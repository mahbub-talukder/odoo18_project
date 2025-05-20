# Website SEO Multi-Website Selector

This module enhances the Odoo 18 Website SEO functionality by adding a website selector to the Optimize SEO interface. This allows administrators to manage SEO settings for all websites from a single interface, rather than having to switch between websites.

## Features

1. **Website Selector Dropdown**: Adds a dropdown in the Optimize SEO dialog to select from available websites.
2. **Context-Aware SEO Data**: Displays and updates SEO metadata (title, description, keywords) for the selected website.
3. **URL Validation**: Validates that the current page exists on the selected website.
4. **Error Handling**: Shows clear error messages when a page doesn't exist on a selected website.
5. **Permission Control**: Respects existing Odoo permissions for SEO editing.

## Technical Implementation

- Extends the original SEO dialog without modifying core files
- Uses Odoo's patching mechanism to add functionality
- Makes API calls to fetch and save SEO data in the context of the selected website
- Context-aware saving ensures data is stored for the correct website

## Usage

1. Navigate to any page where you can edit SEO (by clicking the Optimize SEO option in the website editor)
2. Use the website selector at the top of the dialog to choose a website
3. Edit the SEO metadata as usual
4. Click Save to apply changes to the selected website

## Requirements

- Odoo 18
- Website module

## Installation

Install like any other Odoo module:

1. Place the module in your addons folder
2. Update the module list
3. Install the "Website SEO Multi-Website Selector" module

## License

LGPL-3 