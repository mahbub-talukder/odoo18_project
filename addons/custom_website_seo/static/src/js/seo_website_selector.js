/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { OptimizeSEODialog } from '@website/components/dialog/seo';
import { seoContext } from '@website/components/dialog/seo';
import { useState, onWillStart, onMounted } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";
import { templates } from "@web/core/templates";
import { xml } from "@odoo/owl";

patch(OptimizeSEODialog.prototype, {
    setup() {
        // Call the original setup first
        super.setup();
        
        // Main SEO data state (single source of truth)
        this.seoData = useState({
            website_meta_title: '',
            website_meta_description: '',
            website_meta_keywords: '',
            website_meta_og_img: '',
            seo_name: '',
            website_indexed: false,
            // Add more fields as needed
        });
        
        // Add website selector state
        this.websiteState = useState({
            websites: [],
            selectedWebsiteId: null,
            loading: false,
            error: null,
            validationError: null
        });
        
        // Add information about the current website to the state
        this.currentWebsiteId = this.website?.currentWebsite?.id;
        
        // Bind methods
        this.onWebsiteChange = this.onWebsiteChange.bind(this);
        this.injectWebsiteSelector = this.injectWebsiteSelector.bind(this);
        this.resetToCurrentWebsiteData = this.resetToCurrentWebsiteData.bind(this);
        this.originalSave = this.save;
        this.save = this.customSave.bind(this);
        
        // Extend onWillStart to load websites
        onWillStart(async () => {
            try {
                // Load list of websites
                this.websiteState.loading = true;
                const websites = await rpc('/website/get_websites');
                this.websiteState.websites = websites;
                
                // Set the current website as selected by default
                if (this.currentWebsiteId) {
                    this.websiteState.selectedWebsiteId = this.currentWebsiteId;
                } else if (websites && websites.length > 0) {
                    this.websiteState.selectedWebsiteId = websites[0].id;
                    this.currentWebsiteId = websites[0].id;
                }
                
                // Fetch initial SEO data for the current website
                // await this.fetchAndSetSeoData(this.websiteState.selectedWebsiteId);
                
                this.websiteState.loading = false;
            } catch (error) {
                this.websiteState.error = _t('Failed to load websites');
                this.websiteState.loading = false;
                console.error('Error loading websites:', error);
            }
        });
        
        // Inject website selector on mount
        onMounted(async () => {
            let attempts = 0;
            const maxAttempts = 20;
            const tryInject = () => {
                const dialogContent = document.querySelector('.modal .modal-body');
                if (dialogContent) {
                    this.injectWebsiteSelector();
                } else if (attempts < maxAttempts) {
                    attempts += 1;
                    setTimeout(tryInject, 100);
                } else {
                    console.warn('Website selector injection failed: dialog not found.');
                }
            };
            tryInject();
            await this.fetchAndSetSeoData(this.websiteState.selectedWebsiteId);
        });
    },
    
    async fetchAndSetSeoData(websiteId) {
        // Fetch SEO data for the given website and update this.seoData
        try {
            // Get the view_id from this.seoContext or this.object
            let viewId = undefined;
            if (this.seoContext && this.seoContext.viewId) {
                viewId = this.seoContext.viewId;
            } else if (this.object && this.object.viewIds && this.object.viewIds.length > 0) {
                viewId = this.object.viewIds[0];
            } else if (this.object && this.object.view_id) {
                viewId = this.object.view_id;
            }
            
            console.log(`Fetching SEO data for website ${websiteId} with view_id ${viewId}`);
            
            const seoData = await rpc('/website/get_seo_data_for_website', {
                'res_id': this.object.id,
                'res_model': this.object.model,
                'view_id': viewId,
                'website_id': websiteId
            });
            
            console.log(`Received SEO data for website ${websiteId}:`, seoData);
            
            // Handle error response
            if (seoData.error) {
                console.error(`Error fetching SEO data: ${seoData.error}`);
                this.websiteState.error = seoData.error;
                return;
            }
            
            // Initialize defaults for all fields
            const defaultValues = {
                website_meta_title: '',
                website_meta_description: '',
                website_meta_keywords: '',
                website_meta_og_img: '',
                seo_name: '',
                website_indexed: false
            };
            
            // Update this.seoData with values from response or defaults
            Object.keys(defaultValues).forEach(key => {
                // Only update if the key exists in our state
                if (key in this.seoData) {
                    this.seoData[key] = seoData[key] !== undefined ? seoData[key] : defaultValues[key];
                }
            });
            
            console.log(`Updated SEO data state:`, this.seoData);
            
            // Now update the actual form fields to reflect the new data
            this.updateFormFields(this.seoData);
            
            // Add real-time preview update listeners
            this.addPreviewUpdateListeners();
            
        } catch (error) {
            console.error('Failed to fetch SEO data:', error);
            this.websiteState.error = _t('Error fetching SEO data');
        }
    },
    
    /**
     * Add event listeners to input fields to update preview in real-time
     */
    addPreviewUpdateListeners() {
        // Find input fields by their label's for attribute
        const titleField = document.querySelector('.modal .modal-body label[for="website_meta_title"] + input');
        const descField = document.querySelector('.modal .modal-body label[for="website_meta_description"] + textarea');
        
        // Add input event listener to title field
        if (titleField) {
            titleField.addEventListener('input', () => {
                this.updatePreviews({
                    website_meta_title: titleField.value
                });
            });
            console.log('Added input listener to title field');
        }
        
        // Add input event listener to description field
        if (descField) {
            descField.addEventListener('input', () => {
                this.updatePreviews({
                    website_meta_description: descField.value
                });
            });
            console.log('Added input listener to description field');
        }
    },
    
    /**
     * Update preview elements with the provided data
     * @param {Object} data Data containing title and/or description
     */
    updatePreviews(data) {
        // Update the preview title
        if (data.website_meta_title !== undefined) {
            const previewTitle = document.querySelector('.modal .modal-body .oe_seo_preview_g .r');
            if (previewTitle) {
                previewTitle.textContent = data.website_meta_title || 'Title';
            }
            
            // Update the social preview title
            const socialTitle = document.querySelector('.modal .modal-body .card-title');
            if (socialTitle) {
                socialTitle.textContent = data.website_meta_title || 'Title';
            }
        }
        
        // Update the preview description
        if (data.website_meta_description !== undefined) {
            const previewDesc = document.querySelector('.modal .modal-body .oe_seo_preview_g .st');
            if (previewDesc) {
                previewDesc.textContent = data.website_meta_description || 'Description';
            }
            
            // Update the social preview description
            const socialDesc = document.querySelector('.modal .modal-body .card-body p');
            if (socialDesc) {
                socialDesc.textContent = data.website_meta_description || 'Description';
            }
        }
    },
    
    /**
     * Update all form fields with values from the seoData object
     * @param {Object} data The SEO data to set in the form fields
     */
    async updateFormFields(data) {
        console.log('Updating form fields with:', data);
        
        // Find title field by its label's for attribute (more specific)
        const titleField = document.querySelector('.modal .modal-body label[for="website_meta_title"] + input');
        if (titleField) {
            titleField.value = data.website_meta_title || '';
            console.log('Updated title field:', titleField.value);
        } else {
            console.warn('Title field not found');
            setTimeout(() => {
                this.updateFormFields(data);
                
            }, 100);
        }
        
        // Find description field by its label's for attribute (more specific)
        const descField = document.querySelector('.modal .modal-body label[for="website_meta_description"] + textarea');
        if (descField) {
            descField.value = data.website_meta_description || '';
            console.log('Updated description field:', descField.value);
        } else {
            console.warn('Description field not found');
        }
        
        // Update keywords table if data contains keywords
        if (data.website_meta_keywords) {
            this.updateKeywords(data.website_meta_keywords);
        }
        
        // Update social preview image if OG image data is available
        if (data.website_meta_og_img) {
            this.updateSocialImage(data.website_meta_og_img);
        }
        
        // Update previews
        this.updatePreviews(data);
        
        // Keywords and other fields are handled by their own components in Odoo
        // We can't easily update them directly
        
        console.log('Form fields updated');
    },
    
    /**
     * Get values from the form fields
     * @returns {Object} The SEO data from the form fields
     */
    getFormValues() {
        const data = {};
        
        // Find title field by its label's for attribute (more specific)
        const titleField = document.querySelector('.modal .modal-body label[for="website_meta_title"] + input');
        if (titleField) {
            data.website_meta_title = titleField.value;
            console.log('Retrieved title:', data.website_meta_title);
        } else {
            console.warn('Title field not found for retrieval');
        }
        
        // Find description field by its label's for attribute (more specific)
        const descField = document.querySelector('.modal .modal-body label[for="website_meta_description"] + textarea');
        if (descField) {
            data.website_meta_description = descField.value;
            console.log('Retrieved description:', data.website_meta_description);
        } else {
            console.warn('Description field not found for retrieval');
        }
        
        // Keywords are handled by their component in Odoo
        // We need to get them from the table instead of an input field
        const keywordRows = document.querySelectorAll('.modal .modal-body .table-responsive table tr');
        if (keywordRows && keywordRows.length > 1) {  // Skip header row
            const keywords = [];
            // Start from index 1 to skip the header row
            for (let i = 1; i < keywordRows.length; i++) {
                const keywordCell = keywordRows[i].querySelector('td');
                if (keywordCell && keywordCell.textContent.trim()) {
                    keywords.push(keywordCell.textContent.trim());
                }
            }
            data.website_meta_keywords = keywords.join(', ');
            console.log('Retrieved keywords:', data.website_meta_keywords);
        } else {
            console.warn('Keyword table not found or empty');
        }
        
        // OG Image is handled by its component
        // We need to get the src from the active image
        const activeImage = document.querySelector('.modal .modal-body .o_active_image img');
        if (activeImage && activeImage.src) {
            data.website_meta_og_img = activeImage.src;
            console.log('Retrieved OG image:', data.website_meta_og_img);
        } else {
            console.warn('Active OG image not found');
        }
        
        console.log('Form values retrieved:', data);
        return data;
    },
    
    /**
     * Inject the website selector into the dialog
     */
    injectWebsiteSelector() {
        const dialogContent = document.querySelector('.modal .modal-body');
        if (!dialogContent || document.getElementById('website_selector_container')) {
            return;
        }
        
        // Create website selector container
        const selectorContainer = document.createElement('section');
        selectorContainer.id = 'website_selector_container';
        selectorContainer.className = 'mb-4 row';
        const colDiv = document.createElement('div');
        colDiv.className = 'col-12';
        selectorContainer.appendChild(colDiv);
        
        // Create label
        const label = document.createElement('label');
        label.setAttribute('for', 'website_selector');
        label.textContent = 'Website';
        colDiv.appendChild(label);
        
        // Create input group
        const inputGroup = document.createElement('div');
        inputGroup.className = 'input-group';
        
        // Create select element
        const select = document.createElement('select');
        select.id = 'website_selector';
        select.className = 'form-control';
        select.disabled = this.websiteState.loading;
        select.addEventListener('change', this.onWebsiteChange);
        
        // Add options for each website
        this.websiteState.websites.forEach(website => {
            const option = document.createElement('option');
            option.value = website.id;
            option.textContent = website.name;
            option.selected = website.id === this.websiteState.selectedWebsiteId;
            select.appendChild(option);
        });
        
        inputGroup.appendChild(select);
        
        // Add loading indicator if needed
        if (this.websiteState.loading) {
            const loadingAppend = document.createElement('div');
            loadingAppend.className = 'input-group-append';
            const loadingSpan = document.createElement('span');
            loadingSpan.className = 'input-group-text';
            const loadingIcon = document.createElement('i');
            loadingIcon.className = 'fa fa-spin fa-spinner';
            loadingSpan.appendChild(loadingIcon);
            loadingAppend.appendChild(loadingSpan);
            inputGroup.appendChild(loadingAppend);
        }
        
        colDiv.appendChild(inputGroup);
        
        // Add error message if needed
        if (this.websiteState.error) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'alert alert-danger mt-2';
            errorDiv.textContent = this.websiteState.error;
            colDiv.appendChild(errorDiv);
        }
        
        // Add validation error if needed
        if (this.websiteState.validationError) {
            const validationDiv = document.createElement('div');
            validationDiv.className = 'alert alert-warning mt-2';
            validationDiv.textContent = this.websiteState.validationError;
            colDiv.appendChild(validationDiv);
        }
        
        // Add info message if editing a different website
        if (this.websiteState.selectedWebsiteId !== this.currentWebsiteId) {
            const infoDiv = document.createElement('div');
            infoDiv.className = 'alert alert-info mt-2';
            const infoIcon = document.createElement('i');
            infoIcon.className = 'fa fa-info-circle';
            infoDiv.appendChild(infoIcon);
            infoDiv.appendChild(document.createTextNode(' You are editing SEO data for a different website.'));
            colDiv.appendChild(infoDiv);
        }
        
        // Insert at the beginning of the dialog
        const firstSection = dialogContent.querySelector('section');
        if (firstSection) {
            dialogContent.insertBefore(selectorContainer, firstSection);
        } else {
            dialogContent.insertBefore(selectorContainer, dialogContent.firstChild);
        }
        console.log('Website selector injected!');
    },
    
    /**
     * Handle website selection change
     */
    async onWebsiteChange(ev) {
        const websiteId = parseInt(ev.target.value, 10);
        console.log(`Website changed to: ${websiteId}`);
        this.websiteState.selectedWebsiteId = websiteId;
        this.websiteState.validationError = null;
        
        // Update the UI to reflect the selection
        const infoContainer = document.getElementById('website_selector_container');
        if (infoContainer) {
            // Remove existing messages
            const existingMessages = infoContainer.querySelectorAll('.alert');
            existingMessages.forEach(msg => msg.remove());
            
            // Add loading indicator
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'alert alert-info mt-2';
            const loadingIcon = document.createElement('i');
            loadingIcon.className = 'fa fa-spin fa-spinner';
            loadingDiv.appendChild(loadingIcon);
            loadingDiv.appendChild(document.createTextNode(' Loading SEO data...'));
            infoContainer.appendChild(loadingDiv);
        }
        
        if (websiteId !== this.currentWebsiteId) {
            try {
                this.websiteState.loading = true;
                
                // Fetch and update SEO data for the selected website
                await this.fetchAndSetSeoData(websiteId);
                
                this.websiteState.loading = false;
                
                // Update UI to show different website message
                if (infoContainer) {
                    // Remove loading indicator
                    const existingMessages = infoContainer.querySelectorAll('.alert');
                    existingMessages.forEach(msg => msg.remove());
                    
                    // Add info message if editing a different website
                    if (this.websiteState.selectedWebsiteId !== this.currentWebsiteId) {
                        const infoDiv = document.createElement('div');
                        infoDiv.className = 'alert alert-info mt-2';
                        const infoIcon = document.createElement('i');
                        infoIcon.className = 'fa fa-info-circle';
                        infoDiv.appendChild(infoIcon);
                        infoDiv.appendChild(document.createTextNode(' You are editing SEO data for a different website.'));
                        infoContainer.appendChild(infoDiv);
                    }
                }
            } catch (error) {
                this.websiteState.error = _t('Failed to load SEO data for selected website');
                this.websiteState.loading = false;
                console.error('Error loading SEO data:', error);
                
                // Update UI with error message
                if (infoContainer) {
                    // Remove loading indicator
                    const existingMessages = infoContainer.querySelectorAll('.alert');
                    existingMessages.forEach(msg => msg.remove());
                    
                    // Add error message
                    const errorDiv = document.createElement('div');
                    errorDiv.className = 'alert alert-danger mt-2';
                    errorDiv.textContent = this.websiteState.error;
                    infoContainer.appendChild(errorDiv);
                }
            }
        } else {
            // If the model is product.template, fetch and set SEO data
            console.log('Model:', this.object.model);
            if (this.object.model === 'product.template') {
                await this.fetchAndSetSeoData(websiteId);
            } else {
                // Reset to original SEO data for current website (for other models)
                await this.resetToCurrentWebsiteData();
            }
            
            // Update UI to remove different website message
            if (infoContainer) {
                // Remove messages
                const existingMessages = infoContainer.querySelectorAll('.alert');
                existingMessages.forEach(msg => msg.remove());
            }
        }
    },
    
    /**
     * Reset data to current website values
     */
    async resetToCurrentWebsiteData() {
        try {
            // Refetch original data for current website
            const data = await rpc('/website/get_seo_data', {
                'res_id': this.object.id,
                'res_model': this.object.model,
            });
            
            // Update all fields in this.seoData
            Object.keys(this.seoData).forEach(key => {
                this.seoData[key] = data[key] !== undefined ? data[key] : '';
            });
            
            // Update the form fields
            this.updateFormFields(this.seoData);
        } catch (error) {
            console.error('Error resetting SEO data:', error);
        }
    },
    
    /**
     * Custom save method to handle saving to a different website
     */
    async customSave() {
        // Get values from form fields
        const data = this.getFormValues();
        // Print values for debugging
        console.log("Saving SEO data:", data);
        // Get the selected website
        const selectedWebsite = this.websiteState.websites.find(
            website => website.id === this.websiteState.selectedWebsiteId
        );
        console.log(`Selected website: ${selectedWebsite?.name} (ID: ${this.websiteState.selectedWebsiteId})`);
        
        // Get the view_id from this.seoContext or this.object
        let viewId = undefined;
        if (this.seoContext && this.seoContext.viewId) {
            viewId = this.seoContext.viewId;
        } else if (this.object && this.object.viewIds && this.object.viewIds.length > 0) {
            viewId = this.object.viewIds[0];
        } else if (this.object && this.object.view_id) {
            viewId = this.object.view_id;
        }
        
        console.log(`Saving SEO data with view_id ${viewId}`);
        
        try {
            // If we're saving to the current website, use the original save method
            if (this.websiteState.selectedWebsiteId === this.currentWebsiteId && this.object.model != 'product.template') {
                console.log("Saving to current website using original save method");
                await this.originalSave();
                return;
            }
            // Check if we have any SEO data to save
            if (Object.keys(data).length === 0) {
                console.error("No SEO data to save");
                this.websiteState.error = _t('No SEO data to save');
                // Show error in UI
                const infoContainer = document.getElementById('website_selector_container');
                if (infoContainer) {
                    // Remove existing messages
                    const existingMessages = infoContainer.querySelectorAll('.alert');
                    existingMessages.forEach(msg => msg.remove());
                    // Add error message
                    const errorDiv = document.createElement('div');
                    errorDiv.className = 'alert alert-danger mt-2';
                    errorDiv.textContent = this.websiteState.error;
                    infoContainer.appendChild(errorDiv);
                }
                return;
            }
            // Show saving indicator
            const infoContainer = document.getElementById('website_selector_container');
            if (infoContainer) {
                // Remove existing messages
                const existingMessages = infoContainer.querySelectorAll('.alert');
                existingMessages.forEach(msg => msg.remove());
                // Add loading message
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'alert alert-info mt-2';
                const loadingIcon = document.createElement('i');
                loadingIcon.className = 'fa fa-spin fa-spinner';
                loadingDiv.appendChild(loadingIcon);
                loadingDiv.appendChild(document.createTextNode(' Saving SEO data...'));
                infoContainer.appendChild(loadingDiv);
            }
            // If we're saving to a different website, use RPC to save the data with the correct context
            console.log("Saving to different website using RPC");
            const result = await rpc('/website/seo_save', {
                'res_id': this.object.id,
                'res_model': this.object.model,
                'view_id': viewId,
                'website_id': this.websiteState.selectedWebsiteId,
                'data': data,
                'lang': selectedWebsite?.lang || this.website?.currentWebsite?.lang || 'en_US',
            });
            console.log("Save result:", result);
            if (result && result.error) {
                this.websiteState.error = _t('Error: ') + result.error;
                console.error(`Error saving SEO data: ${result.error}`);
                // Show error in UI
                if (infoContainer) {
                    // Remove existing messages
                    const existingMessages = infoContainer.querySelectorAll('.alert');
                    existingMessages.forEach(msg => msg.remove());
                    // Add error message
                    const errorDiv = document.createElement('div');
                    errorDiv.className = 'alert alert-danger mt-2';
                    errorDiv.textContent = this.websiteState.error;
                    infoContainer.appendChild(errorDiv);
                }
                return;
            }
            if (result && result.warning) {
                console.warn(`Warning saving SEO data: ${result.warning}`);
            }
            if (result && result.saved_values) {
                console.log("Saved values confirmed:", result.saved_values);
            }
            // Show success message
            if (infoContainer) {
                // Remove existing messages
                const existingMessages = infoContainer.querySelectorAll('.alert');
                existingMessages.forEach(msg => msg.remove());
                // Add success message
                const successDiv = document.createElement('div');
                successDiv.className = 'alert alert-success mt-2';
                successDiv.textContent = _t('SEO data saved successfully!');
                infoContainer.appendChild(successDiv);
                // Automatically close after a few seconds
                setTimeout(() => {
                    if (this.props.close) {
                        this.props.close();
                    }
                }, 1500);
            } else {
                // If no container for messages, just close the dialog
                if (this.props.close) {
                    this.props.close();
                }
            }
        } catch (error) {
            console.error('Error saving SEO data:', error);
            // Show error message to user
            this.websiteState.error = _t('Failed to save SEO data');
            // Show error in UI
            const infoContainer = document.getElementById('website_selector_container');
            if (infoContainer) {
                // Remove existing messages
                const existingMessages = infoContainer.querySelectorAll('.alert');
                existingMessages.forEach(msg => msg.remove());
                // Add error message
                const errorDiv = document.createElement('div');
                errorDiv.className = 'alert alert-danger mt-2';
                errorDiv.textContent = this.websiteState.error;
                infoContainer.appendChild(errorDiv);
            }
        }
    },
    
    /**
     * Update the keywords table with the given keywords string
     * @param {String} keywordsStr Comma-separated keywords
     */
    updateKeywords(keywordsStr) {
        try {
            if (!keywordsStr) return;
            
            console.log('Updating keywords table with:', keywordsStr);
            
            // Clear existing keywords by clicking all remove buttons
            this.clearExistingKeywords();
            
            // Wait for the table to clear
            setTimeout(() => {
                // Add each keyword
                const keywords = keywordsStr.split(',').map(k => k.trim()).filter(k => k);
                
                if (keywords.length > 0) {
                    this.addKeywords(keywords);
                }
            }, 100);
        } catch (error) {
            console.error('Error updating keywords:', error);
        }
    },
    
    /**
     * Clear all existing keywords in the table
     */
    clearExistingKeywords() {
        try {
            const keywordRows = document.querySelectorAll('.modal .modal-body .table-responsive table tr');
            if (keywordRows && keywordRows.length > 1) {
                // Skip header row, start from index 1
                for (let i = 1; i < keywordRows.length; i++) {
                    const removeButton = keywordRows[i].querySelector('a.oe_remove');
                    if (removeButton) {
                        removeButton.click();
                        console.log('Removed keyword row');
                    }
                }
            }
        } catch (error) {
            console.error('Error clearing keywords:', error);
        }
    },
    
    /**
     * Add keywords one by one
     * @param {Array} keywords Array of keywords to add
     */
    addKeywords(keywords) {
        if (!keywords || keywords.length === 0) return;
        
        try {
            // Find the keyword input and add button
            const keywordInput = document.querySelector('.modal .modal-body input[placeholder="Keyword"]');
            const addButton = keywordInput?.parentElement?.querySelector('button.btn-primary');
            
            if (keywordInput && addButton) {
                // Function to add a keyword
                const addKeyword = (keyword, index) => {
                    setTimeout(() => {
                        // Set the keyword in the input
                        keywordInput.value = keyword;
                        
                        // Trigger input event to make sure Odoo's handlers know the value changed
                        keywordInput.dispatchEvent(new Event('input', { bubbles: true }));
                        
                        // Click the add button
                        setTimeout(() => {
                            addButton.click();
                            console.log(`Added keyword: ${keyword}`);
                        }, 50);
                    }, index * 200); // Add slight delay between keywords
                };
                
                // Add each keyword with a delay
                keywords.forEach((keyword, index) => {
                    addKeyword(keyword, index);
                });
            } else {
                console.warn('Keyword input or add button not found');
            }
        } catch (error) {
            console.error('Error adding keywords:', error);
        }
    },
    
    /**
     * Update the social preview image
     * @param {String} imageSrc URL of the image to set
     */
    updateSocialImage(imageSrc) {
        try {
            if (!imageSrc) return;
            
            console.log('Updating social preview image with:', imageSrc);
            
            // Find all image elements in the metadata images section
            const metaImages = document.querySelectorAll('.modal .modal-body .o_seo_og_image .o_meta_img img');
            
            // Find the active image marker
            const activeImageContainer = document.querySelector('.modal .modal-body .o_seo_og_image .o_active_image');
            
            // Find the actual preview image in the social preview card
            const socialPreviewImage = document.querySelector('.modal .modal-body .card-img-top.o_meta_active_img');
            
            // Check if the image already exists in the options
            let imageFound = false;
            let imageElement = null;
            
            metaImages.forEach(img => {
                if (img.src === imageSrc) {
                    imageFound = true;
                    imageElement = img;
                    console.log('Found matching image in options');
                }
            });
            
            // If we found the image, simulate clicking it to make it active
            if (imageFound && imageElement) {
                // Handle the case where we need to make it active
                const imgContainer = imageElement.closest('.o_meta_img');
                if (imgContainer && !imgContainer.classList.contains('o_active_image')) {
                    // Remove active class from current active container
                    if (activeImageContainer) {
                        activeImageContainer.classList.remove('o_active_image');
                    }
                    
                    // Add active class to the new container
                    imgContainer.classList.add('o_active_image');
                    
                    // Update the preview image
                    if (socialPreviewImage) {
                        socialPreviewImage.src = imageSrc;
                        console.log('Updated social preview image');
                    }
                }
            } else {
                // If image not found in options, just update the preview directly
                if (socialPreviewImage) {
                    socialPreviewImage.src = imageSrc;
                    console.log('Updated social preview image directly');
                }
                
                // If there's an active container, attempt to update its image
                if (activeImageContainer) {
                    const activeImg = activeImageContainer.querySelector('img');
                    if (activeImg) {
                        activeImg.src = imageSrc;
                        console.log('Updated active image container');
                    }
                }
            }
        } catch (error) {
            console.error('Error updating social image:', error);
        }
    }
});

