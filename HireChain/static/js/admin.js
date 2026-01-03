/**
 * HireChain - Admin Panel JavaScript
 * Handles applicant management functionality
 * Follows Single Responsibility Principle
 */

let currentApplicationId = null;

// Applicant Modal Management
class ApplicantModalManager {
    constructor() {
        this.modal = document.getElementById('applicantModal');
    }
    
    async openModal(applicationId) {
        currentApplicationId = applicationId;
        await this.loadApplicationDetails(applicationId);
    }
    
    closeModal() {
        if (this.modal) {
            this.modal.classList.remove('show');
        }
        currentApplicationId = null;
    }
    
    async loadApplicationDetails(applicationId) {
        try {
            const csrfToken = getCookie('csrftoken');
            const response = await fetch(`/applications/api/application/${applicationId}/`, {
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });
            
            if (!response.ok) throw new Error('Failed to load application details');
            
            const application = await response.json();
            
            // Populate modal
            document.getElementById('detailFullName').textContent = application.full_name;
            document.getElementById('detailEmail').textContent = application.email;
            document.getElementById('detailEmail').href = `mailto:${application.email}`;
            document.getElementById('detailPhone').textContent = application.phone;
            document.getElementById('detailPhone').href = `tel:${application.phone}`;
            
            const linkedinElement = document.getElementById('detailLinkedin');
            if (application.linkedin) {
                linkedinElement.textContent = application.linkedin;
                linkedinElement.href = application.linkedin;
                linkedinElement.style.display = 'inline';
            } else {
                linkedinElement.textContent = 'Not provided';
                linkedinElement.style.display = 'inline';
                linkedinElement.removeAttribute('href');
            }
            
            const portfolioElement = document.getElementById('detailPortfolio');
            if (application.portfolio) {
                portfolioElement.innerHTML = `<a href="${application.portfolio}" target="_blank" class="info-link">${application.portfolio}</a>`;
            } else {
                portfolioElement.textContent = 'Not provided';
            }
            
            const coverLetterElement = document.getElementById('detailCoverLetter');
            if (application.cover_letter) {
                coverLetterElement.textContent = application.cover_letter;
            } else {
                coverLetterElement.textContent = 'No cover letter provided';
            }
            
            // Handle resume download checkbox
            const downloadCheckbox = document.getElementById('downloadResumeCheck');
            if (application.resume_url) {
                downloadCheckbox.parentElement.style.display = 'flex';
                downloadCheckbox.onclick = () => {
                    if (downloadCheckbox.checked) {
                        window.open(application.resume_url, '_blank');
                        setTimeout(() => {
                            downloadCheckbox.checked = false;
                        }, 1000);
                    }
                };
            } else {
                downloadCheckbox.parentElement.style.display = 'none';
            }
            
            // Show modal
            this.modal.classList.add('show');
            
        } catch (error) {
            console.error('Error loading application details:', error);
            alert('Failed to load application details. Please try again.');
        }
    }
}

// Status Update Management
class StatusUpdateManager {
    static async updateStatus(newStatus) {
        if (!currentApplicationId) {
            alert('No application selected');
            return;
        }
        
        const csrfToken = getCookie('csrftoken');
        const formData = new FormData();
        formData.append('status', newStatus);
        
        try {
            const response = await fetch(`/applications/api/application/${currentApplicationId}/update-status/`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });
            
            const data = await response.json();
            
            if (data.success) {
                alert('Status updated successfully!');
                
                // Update status badge in table
                const row = document.querySelector(`tr[data-application-id="${currentApplicationId}"]`);
                if (row) {
                    const statusBadge = row.querySelector('.badge');
                    if (statusBadge) {
                        // Remove old status class
                        statusBadge.className = 'badge';
                        // Add new status class
                        statusBadge.classList.add(`badge-${newStatus}`);
                        // Update text
                        statusBadge.textContent = newStatus.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
                    }
                }
                
                applicantModalManager.closeModal();
            } else {
                alert(data.message || 'Failed to update status');
            }
        } catch (error) {
            console.error('Error updating status:', error);
            alert('An error occurred while updating the status. Please try again.');
        }
    }
}

// Search and Filter Management
class AdminSearchManager {
    constructor() {
        this.searchInput = document.getElementById('searchInput');
        this.filterBtn = document.getElementById('filterBtn');
        this.init();
    }
    
    init() {
        if (this.searchInput) {
            this.searchInput.addEventListener('input', () => this.filterTable());
        }
    }
    
    filterTable() {
        const searchTerm = this.searchInput.value.toLowerCase();
        const rows = document.querySelectorAll('.applicant-row');
        
        rows.forEach(row => {
            const name = row.cells[0]?.textContent.toLowerCase() || '';
            const job = row.cells[1]?.textContent.toLowerCase() || '';
            const email = row.cells[2]?.textContent.toLowerCase() || '';
            
            const matches = name.includes(searchTerm) || 
                          job.includes(searchTerm) || 
                          email.includes(searchTerm);
            
            row.style.display = matches ? '' : 'none';
        });
    }
}

// Global functions for onclick handlers
let applicantModalManager;

function viewApplicationDetails(applicationId) {
    applicantModalManager.openModal(applicationId);
}

function closeApplicantModal() {
    applicantModalManager.closeModal();
}

function updateStatus(status) {
    StatusUpdateManager.updateStatus(status);
}

// Utility function
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

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    applicantModalManager = new ApplicantModalManager();
    new AdminSearchManager();
});
