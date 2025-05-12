# Odoo 18 with Docker Compose

This project sets up Odoo 18 with PostgreSQL using Docker Compose, including a custom module for unified sales automation.

## Requirements

- Docker and Docker Compose installed on your system
- Basic knowledge of Docker and Odoo

## Getting Started

1. Clone this repository
2. Navigate to the project directory

```bash
cd odoo18_docker
```

3. Start the containers

```bash
docker-compose up -d
```

4. Access Odoo through your web browser:

```
http://localhost:8069
```

## Project Structure

```
odoo18_docker/
├── docker-compose.yml      # Docker Compose configuration
├── addons/                 # Custom Odoo modules directory
│   └── unified_sales/      # Unified Sales module
└── README.md               # This file
```

## Custom Module: Unified Sales

The Unified Sales module provides:

1. Integration with external e-commerce platforms (e.g., Shopify) to create quotations from external orders.
2. Automated sales workflow when payments are confirmed:
   - Confirm the corresponding quotation (on LIFO basis)
   - Create and confirm the sales order
   - Generate and validate the invoice
   - Reconcile the payment with the invoice

## Configuration

After installing the module:

1. Go to Unified Sales > API Configurations
2. Create a new API configuration for your external platform
3. Use the generated webhook URL in your external platform to send order data to Odoo

## Logs and Troubleshooting

To view the container logs:

```bash
docker-compose logs -f odoo
```

## Data Persistence

The PostgreSQL data is stored in a Docker volume and persists across container restarts.

## Stopping the Containers

```bash
docker-compose down
```

To remove volumes and start fresh:

```bash
docker-compose down -v
``` 