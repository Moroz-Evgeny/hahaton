document.addEventListener('DOMContentLoaded', () => {
	const container = document.querySelector('.container_')
	var date = container.dataset.date
	var carbon_ratio = container.dataset.ratio

	console.log('date:', date)
	console.log('carbon_ratio:', carbon_ratio)
})
