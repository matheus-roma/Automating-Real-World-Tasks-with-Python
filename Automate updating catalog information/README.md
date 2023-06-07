# Project Problem Statement
Week 4 of Automating Real-World Tasks with Python

The premisse of this task it's that you work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, it should:

- Upload the new products to the online store. Images and descriptions should be uploaded separately, using two different web endpoints.

- Send a report back to the supplier, letting them know what you imported.

Since this process is key to the business's success, you need to make sure that it keeps running! So, you’ll also:

- Run a script on your web server to monitor system health.

- Send an email with an alert if the server is ever unhealthy.