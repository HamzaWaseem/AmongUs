#!/bin/bash

# Set the base URL
BASE_URL="http://localhost:8000"
TARGET_URL="https://example.com"

echo "Testing CSRF Service Endpoints..."
echo "================================"
echo "1. Testing CSRF Check endpoint"
curl -X POST \
  "${BASE_URL}/service_csrf/check/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=${TARGET_URL}"
echo -e "\n"

echo "2. Testing CSRF Report endpoint"
curl -X GET \
  "${BASE_URL}/service_csrf/report/?url=${TARGET_URL}"
echo -e "\n"

echo "Testing XSS Service Endpoints..."
echo "==============================="
echo "1. Testing XSS Scan endpoint"
curl -X POST \
  "${BASE_URL}/service_xss/scan/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=${TARGET_URL}"
echo -e "\n"

echo "2. Testing XSS Report endpoint"
curl -X GET \
  "${BASE_URL}/service_xss/report/?url=${TARGET_URL}"
echo -e "\n"

echo "Testing Authentication Service Endpoints..."
echo "========================================="
echo "1. Testing Authentication Analysis endpoint"
curl -X POST \
  "${BASE_URL}/service_authentication/analyze/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=${TARGET_URL}" \
  -d "login_endpoint=/login"
echo -e "\n"

echo "2. Testing Authentication Report endpoint"
curl -X GET \
  "${BASE_URL}/service_authentication/report/?url=${TARGET_URL}"
echo -e "\n" 