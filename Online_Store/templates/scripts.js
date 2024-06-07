// JavaScript to handle modal opening and closing
document.addEventListener('DOMContentLoaded', function () {
    const openModalButtons = document.querySelectorAll('.openModal');
    const closeModalButtons = document.querySelectorAll('.closeModal');

    openModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetModalId = button.getAttribute('data-target');
            const targetModal = document.getElementById(targetModalId);
            targetModal.style.display = 'block';
        });
    });

    closeModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetModalId = button.getAttribute('data-target');
            const targetModal = document.getElementById(targetModalId);
            targetModal.style.display = 'none';
        });
    });
});