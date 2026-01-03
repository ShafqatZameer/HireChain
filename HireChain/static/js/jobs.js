/**
 * HireChain - Jobs Page JavaScript
 * Handles job details modal and application form
 * Follows Single Responsibility Principle
 */

let currentJobId = null;

// Modal Management
class JobModalManager {
    constructor() {
        this.jobModal = document.getElementById('jobModal');
        this.applicationModal = document.getElementById('applicationModal');
    }
    
    openJobModal(jobId) {
        currentJobId = jobId;
        this.loadJobDetails(jobId);
    }
    
    closeJobModal() {
        if (this.jobModal) {
            this.jobModal.classList.remove('show');
        }
    }
    
    openApplicationModal() {
        this.closeJobModal();
        
        // Check if user is authenticated
        const isAuthenticated = document.querySelector('[data-user-authenticated]');
        if (!isAuthenticated) {
            // Redirect to login
            window.location.href = `/accounts/login/?next=${window.location.pathname}`;
            return;
        }
        
        if (this.applicationModal) {
            this.applicationModal.classList.add('show');
            
            // Set job title in application modal
            const jobTitle = document.getElementById('modalJobTitle').textContent;
            document.getElementById('appJobTitle').textContent = jobTitle;
        }
    }
    
    closeApplicationModal() {
        if (this.applicationModal) {
            this.applicationModal.classList.remove('show');
        }
    }
    
    async loadJobDetails(jobId) {
        try {
            const response = await fetch(`/api/job/${jobId}/`);
            if (!response.ok) throw new Error('Failed to load job details');
            
            const job = await response.json();
            
            // Populate modal
            document.getElementById('modalJobTitle').textContent = job.title;
            document.getElementById('modalCompany').textContent = job.company;
            document.getElementById('modalLocation').textContent = job.location;
            document.getElementById('modalJobType').textContent = job.job_type;
            document.getElementById('modalSalary').textContent = job.salary_range || 'Not specified';
            document.getElementById('modalDescription').textContent = job.description;
            
            // Handle optional sections
            const requirementsSection = document.getElementById('requirementsSection');
            if (job.requirements) {
                document.getElementById('modalRequirements').textContent = job.requirements;
                requirementsSection.style.display = 'block';
            } else {
                requirementsSection.style.display = 'none';
            }
            
            const responsibilitiesSection = document.getElementById('responsibilitiesSection');
            if (job.responsibilities) {
                document.getElementById('modalResponsibilities').textContent = job.responsibilities;
                responsibilitiesSection.style.display = 'block';
            } else {
                responsibilitiesSection.style.display = 'none';
            }
            
            // Show modal
            this.jobModal.classList.add('show');
            
        } catch (error) {
            console.error('Error loading job details:', error);
            alert('Failed to load job details. Please try again.');
        }
    }
}

// Application Form Management
class ApplicationFormManager {
    constructor() {
        this.form = document.getElementById('applicationForm');
        this.submitBtn = document.getElementById('submitApplicationBtn');
        this.init();
    }
    
    init() {
        if (this.form) {
            this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        }
    }
    
    async handleSubmit(e) {
        e.preventDefault();
        
        if (!currentJobId) {
            alert('No job selected');
            return;
        }
        
        const formData = new FormData(this.form);
        const csrfToken = getCookie('csrftoken');
        
        // Disable submit button
        this.submitBtn.disabled = true;
        this.submitBtn.textContent = 'Submitting...';
        
        try {
            const response = await fetch(`/applications/apply/${currentJobId}/`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });
            
            const data = await response.json();
            
            if (data.success) {
                alert('Application submitted successfully!');
                modalManager.closeApplicationModal();
                this.form.reset();
            } else {
                let errorMessage = 'Failed to submit application:\n';
                if (data.errors) {
                    for (const [field, errors] of Object.entries(data.errors)) {
                        errorMessage += `${field}: ${errors.join(', ')}\n`;
                    }
                } else if (data.message) {
                    errorMessage = data.message;
                }
                alert(errorMessage);
            }
        } catch (error) {
            console.error('Error submitting application:', error);
            alert('An error occurred while submitting your application. Please try again.');
        } finally {
            this.submitBtn.disabled = false;
            this.submitBtn.textContent = 'Submit Application';
        }
    }
}

// Global functions for onclick handlers
let modalManager;

function viewJobDetails(jobId) {
    modalManager.openJobModal(jobId);
}

function closeJobModal() {
    modalManager.closeJobModal();
}

function applyForJob() {
    modalManager.openApplicationModal();
}

function closeApplicationModal() {
    modalManager.closeApplicationModal();
}

// Utility function (imported from main.js concept)
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
    modalManager = new JobModalManager();
    new ApplicationFormManager();
});
