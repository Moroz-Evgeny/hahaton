document.addEventListener('DOMContentLoaded', () => {
	const container = document.querySelector('.container_')
	// Получаем данные из атрибутов
	var dateStr = container.dataset.date.replace(/'/g, '"') // Заменяем одинарные кавычки на двойные
	var ratioStr = container.dataset.ratio.replace(/'/g, '"') // Заменяем одинарные кавычки на двойные

	var date = JSON.parse(dateStr) // Преобразуем строку в массив
	var carbon_ratio = JSON.parse(ratioStr) // Преобразуем строку в массив

	var chartTooltip = document.getElementById('toolTip').getContext('2d')

	var toolTip = new Chart(chartTooltip, {
		type: 'line',
		data: {
			labels: date,
			datasets: [
				{
					label: 'online tutorial subjects',
					data: carbon_ratio,
					backgroundColor: ['green'],
					borderColor: ['black'],
					borderWidth: 1,
					pointRadius: 3,
				},
			],
		},
		options: {
			responsive: false,
			plugins: {
				legend: {
					display: false,
					position: 'bottom',
					align: 'center',
					labels: {
						color: 'darkred',
						font: {
							weight: 'bold',
						},
					},
				},
			},
		},
	})

	console.log('date:', date)
	console.log('carbon_ratio:', carbon_ratio)
})
