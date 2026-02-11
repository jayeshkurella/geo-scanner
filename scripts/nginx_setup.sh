#!/bin/bash
set -e

# Load environment variables
set -o allexport
source env/.env.dev
set +o allexport

NGINX_CONF="${NGINX_AVAILABLE_PATH}/${APP_NAME}.conf"

echo "=== Creating nginx fullstack config ==="

sudo tee "$NGINX_CONF" > /dev/null <<EOF
server {
    listen 80;
    server_name ${SERVER_NAME};

    root ${FRONTEND_ROOT};
    index index.html;

    location / {
        try_files \$uri \$uri/ /index.html;
    }

    location /api/ {
        proxy_pass http://${BACKEND_HOST}:${BACKEND_PORT}/;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_redirect off;
    }
}
EOF

echo "=== Enabling site ==="
sudo ln -sf "$NGINX_CONF" "${NGINX_ENABLED_PATH}/"

echo "=== Testing nginx configuration ==="
sudo nginx -t

echo "=== Reloading nginx ==="
sudo systemctl reload nginx

echo "🎉 Nginx configuration applied successfully"
