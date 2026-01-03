/**
 * HireChain - Main JavaScript
 * Handles theme toggle, user menu, and alerts
 * Follows Single Responsibility Principle
 */

// Theme Management
class ThemeManager {
    constructor() {
        this.themeToggle = document.getElementById('themeToggle');
        this.currentTheme = localStorage.getItem('theme') || 'light';
        this.init();
    }
    
    init() {
        this.applyTheme(this.currentTheme);
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', () => this.toggleTheme());
        }
    }
    
    applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        this.currentTheme = theme;
    }
    
    toggleTheme() {
        const newTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        this.applyTheme(newTheme);
    }
}

// User Menu Management
class UserMenuManager {
    constructor() {
        this.userMenuBtn = document.getElementById('userMenuBtn');
        this.userDropdown = document.getElementById('userDropdown');
        this.init();
    }
    
    init() {
        if (this.userMenuBtn && this.userDropdown) {
            this.userMenuBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleDropdown();
            });
            
            document.addEventListener('click', () => this.closeDropdown());
        }
    }
    
    toggleDropdown() {
        this.userDropdown.classList.toggle('show');
    }
    
    closeDropdown() {
        if (this.userDropdown) {
            this.userDropdown.classList.remove('show');
        }
    }
}

// Alert Management
class AlertManager {
    static closeAlert(alertElement) {
        alertElement.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            alertElement.remove();
        }, 300);
    }
    
    static init() {
        document.querySelectorAll('.alert-close').forEach(btn => {
            btn.addEventListener('click', function() {
                AlertManager.closeAlert(this.closest('.alert'));
            });
        });
        
        // Auto-dismiss alerts after 5 seconds
        document.querySelectorAll('.alert').forEach(alert => {
            setTimeout(() => {
                if (alert.parentElement) {
                    AlertManager.closeAlert(alert);
                }
            }, 5000);
        });
    }
}

// Add slideOut animation to CSS dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Search Functionality
class SearchManager {
    constructor() {
        this.searchInput = document.getElementById('jobSearch');
        this.searchBtn = document.querySelector('.search-btn');
        this.init();
    }
    
    init() {
        if (this.searchBtn) {
            this.searchBtn.addEventListener('click', () => this.performSearch());
        }
        
        if (this.searchInput) {
            this.searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.performSearch();
                }
            });
            
            // Real-time search
            this.searchInput.addEventListener('input', () => this.filterJobs());
        }
    }
    
    performSearch() {
        const query = this.searchInput.value.trim();
        if (query) {
            this.filterJobs(query);
        }
    }
    
    filterJobs(query = '') {
        const searchTerm = query || this.searchInput.value;
        const jobCards = document.querySelectorAll('.job-card');
        const lowerSearch = searchTerm.toLowerCase();
        
        jobCards.forEach(card => {
            const title = card.querySelector('.job-title')?.textContent.toLowerCase() || '';
            const company = card.querySelector('.company-name')?.textContent.toLowerCase() || '';
            const location = card.querySelector('.job-location')?.textContent.toLowerCase() || '';
            
            const matches = title.includes(lowerSearch) || 
                          company.includes(lowerSearch) || 
                          location.includes(lowerSearch);
            
            card.style.display = matches ? 'block' : 'none';
        });
    }
}

// Utility Functions
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    new ThemeManager();
    new UserMenuManager();
    AlertManager.init();
    new SearchManager();
});
