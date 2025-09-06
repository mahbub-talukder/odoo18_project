# OX Pricelist Tags

## Overview
This Odoo 18 module allows you to create custom tags for pricelists and display them on product cards for portal users.

## Features
- Create and manage pricelist tags from Sales > Configuration > Pricelist Tags
- Assign multiple tags to pricelists
- Portal users see their assigned pricelist tags on product cards
- Styled tag display with Bootstrap/Odoo standard styling
- Tags appear in the bottom-right corner of product cards

## Installation
1. Copy the module to your Odoo addons directory
2. Update the apps list
3. Install the "OX Pricelist Tags" module

## Usage
1. Go to Sales > Configuration > Pricelist Tags
2. Create tags (e.g., "Premium", "Wholesale", "Discount")
3. Assign tags to pricelists in Sales > Configuration > Pricelists
4. Assign pricelists to contacts
5. Portal users will see the tags on product cards when logged in

## Technical Details
- Depends on: sale, website_sale
- Models: ox.pricelist.tag, product.pricelist (extended)
- Views: Menu, form, tree views for tag management
- Website templates: Product card inheritance for tag display

## Author
OX Solutions
