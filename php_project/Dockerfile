FROM php:7.4-apache

# Copy the PHP project into the Apache document root
COPY . /var/www/html/

# Enable Apache rewrite module
RUN a2enmod rewrite

# Expose port 80
EXPOSE 80

# The Apache server is started by default with this image
