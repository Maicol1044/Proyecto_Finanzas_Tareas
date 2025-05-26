// app/static/js/charts.js

function renderCharts(expensesLabels, expensesValues, incomeLabels, incomeValues) { // Renamed parameters
    // Expenses Chart
    const expensesCtx = document.getElementById('gastosChart'); // Still refers to HTML element ID 'gastosChart'
    if (expensesCtx) {
        new Chart(expensesCtx, {
            type: 'pie',
            data: {
                labels: expensesLabels, // Renamed variable
                datasets: [{
                    data: expensesValues, // Renamed variable
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)',
                        'rgba(255, 159, 64, 0.8)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Expenses by Category' // Updated text
                    }
                }
            }
        });
    }

    // Income Chart
    const incomeCtx = document.getElementById('ingresosChart'); // Still refers to HTML element ID 'ingresosChart'
    if (incomeCtx) {
        new Chart(incomeCtx, {
            type: 'pie',
            data: {
                labels: incomeLabels, // Renamed variable
                datasets: [{
                    data: incomeValues, // Renamed variable
                    backgroundColor: [
                        'rgba(40, 167, 69, 0.8)', // Green
                        'rgba(0, 123, 255, 0.8)', // Blue
                        'rgba(23, 162, 184, 0.8)', // Cyan
                        'rgba(255, 193, 7, 0.8)', // Yellow
                        'rgba(108, 117, 125, 0.8)' // Gray
                    ],
                    borderColor: [
                        'rgba(40, 167, 69, 1)',
                        'rgba(0, 123, 255, 1)',
                        'rgba(23, 162, 184, 1)',
                        'rgba(255, 193, 7, 1)',
                        'rgba(108, 117, 125, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Income by Category' // Updated text
                    }
                }
            }
        });
    }
}