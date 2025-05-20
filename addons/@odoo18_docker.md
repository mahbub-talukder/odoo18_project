
Request:
Customize the Optimize SEO feature in the Website module of Odoo 18 to support multi-website SEO management from a single interface.

🔧 Feature Specification
Current Behavior:
The "Optimize SEO" page only allows editing metadata (title, description, keywords) for the active website.

Desired Enhancement:
Allow users to manage SEO metadata for any website from one interface.

✅ Requirements
1.Add a dropdown listing all websites (website.website model).

2.Upon selecting a website, dynamically load the SEO metadata for the current page in the context of that website.

3.Allow editing and saving SEO metadata as usual.

⚠️ Validation Rules
Ensure that the selected website contains the same relative URL (path after domain) as the current page being edited.

If the URL is not found in the selected website, raise a validation error: "This page does not exist under the selected website. Please choose the correct website."

🧠 Technical Notes
The website dropdown should not trigger a full website switch.

Only load and allow contextual editing of metadata.

Avoid altering the session's active
 


