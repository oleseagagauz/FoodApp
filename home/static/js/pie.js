document.addEventListener('DOMContentLoaded', function () {

    const proteins = parseFloat(document.getElementById('protein').getAttribute('data-protein'));
    const lipids = parseFloat(document.getElementById('lipids').getAttribute('data-lipids'));
    const carbohydrates = parseFloat(document.getElementById('carbohydrates').getAttribute('data-carbohydrates'));


    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Белки', 'Жиры', 'Углеводы'],
            datasets: [{
                data: [proteins, lipids, carbohydrates],
                backgroundColor: [
                    'rgba(0, 255, 0, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)'
                ],
                borderColor: [
                    'rgba(0, 255, 0, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Содержание белков, жиров и углеводов'
            }
        }
    });

});
