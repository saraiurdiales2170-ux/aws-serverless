#!/bin/bash
# Script para automatizar el despliegue del proyecto
sam build
sam deploy --no-confirm-changeset
