document.addEventListener('DOMContentLoaded', () => {
	const container = document.querySelector('.container_')
	const date = container.dataset.date
	const carbon_ratio = container.dataset.ratio

	console.log('date:', date)
	console.log('carbon_ratio:', carbon_ratio)
})
