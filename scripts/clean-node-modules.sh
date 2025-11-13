#!/bin/bash

# Script to clean node_modules directories from the project
# This helps keep the repository clean and avoids accidentally committing dependencies

echo "🧹 Cleaning node_modules directories..."

# Find and remove all node_modules directories
find . -name "node_modules" -type d -prune -exec rm -rf {} +

# Find and remove all package-lock.json files
find . -name "package-lock.json" -type f -delete

echo "✅ node_modules directories and package-lock.json files have been cleaned!"
echo ""
echo "📋 Removed from:"
find . -name "node_modules" -type d -prune | while read dir; do
    echo "   - $dir"
done

echo ""
echo "💡 Note: Run 'npm install' in individual project directories when needed for development."
