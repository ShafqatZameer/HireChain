/**
 * NotificationManager - Handles user notifications
 */
class NotificationManager {
    constructor() {
        this.notificationBtn = document.getElementById('notificationBtn');
        this.notificationDropdown = document.getElementById('notificationDropdown');
        this.notificationList = document.getElementById('notificationList');
        this.notificationBadge = document.getElementById('notificationBadge');
        this.markAllReadBtn = document.getElementById('markAllReadBtn');
        
        if (this.notificationBtn) {
            this.init();
        }
    }
    
    init() {
        // Toggle notification dropdown
        this.notificationBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.notificationDropdown.classList.toggle('show');
            
            // Close user dropdown if open
            const userDropdown = document.getElementById('userDropdown');
            if (userDropdown) {
                userDropdown.classList.remove('show');
            }
        });
        
        // Mark all as read
        if (this.markAllReadBtn) {
            this.markAllReadBtn.addEventListener('click', () => {
                this.markAllAsRead();
            });
        }
        
        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!this.notificationDropdown.contains(e.target) && 
                !this.notificationBtn.contains(e.target)) {
                this.notificationDropdown.classList.remove('show');
            }
        });
        
        // Load notifications on page load
        this.loadNotifications();
        
        // Refresh notifications every 30 seconds
        setInterval(() => {
            this.loadNotifications();
        }, 30000);
    }
    
    async loadNotifications() {
        try {
            const response = await fetch('/applications/api/notifications/');
            if (!response.ok) throw new Error('Failed to load notifications');
            
            const data = await response.json();
            this.updateBadge(data.count);
            this.renderNotifications(data.notifications);
        } catch (error) {
            console.error('Error loading notifications:', error);
        }
    }
    
    updateBadge(count) {
        if (count > 0) {
            this.notificationBadge.textContent = count > 99 ? '99+' : count;
            this.notificationBadge.style.display = 'flex';
        } else {
            this.notificationBadge.style.display = 'none';
        }
    }
    
    renderNotifications(notifications) {
        if (notifications.length === 0) {
            this.notificationList.innerHTML = '<p class="no-notifications">No new notifications</p>';
            return;
        }
        
        this.notificationList.innerHTML = notifications.map(notification => `
            <div class="notification-item" data-id="${notification.id}">
                <div class="notification-content">
                    <p class="notification-message">${notification.message}</p>
                    <p class="notification-time">${notification.created_at}</p>
                </div>
                <button class="notification-close" onclick="notificationManager.markAsRead(${notification.id})">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
                        <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
                    </svg>
                </button>
            </div>
        `).join('');
    }
    
    async markAsRead(notificationId) {
        try {
            const response = await fetch(`/applications/api/notifications/${notificationId}/read/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': this.getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) throw new Error('Failed to mark notification as read');
            
            // Remove notification from DOM
            const notificationItem = document.querySelector(`[data-id="${notificationId}"]`);
            if (notificationItem) {
                notificationItem.remove();
            }
            
            // Reload notifications to update count
            await this.loadNotifications();
        } catch (error) {
            console.error('Error marking notification as read:', error);
        }
    }
    
    async markAllAsRead() {
        try {
            const response = await fetch('/applications/api/notifications/read-all/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': this.getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) throw new Error('Failed to mark all notifications as read');
            
            // Reload notifications
            await this.loadNotifications();
        } catch (error) {
            console.error('Error marking all notifications as read:', error);
        }
    }
    
    getCookie(name) {
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
}

// Initialize notification manager when DOM is loaded
let notificationManager;
document.addEventListener('DOMContentLoaded', () => {
    notificationManager = new NotificationManager();
});
