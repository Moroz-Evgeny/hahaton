document.addEventListener('DOMContentLoaded', () => {
	const container = document.querySelector('.container_')	
	var dateStr = container.dataset.date.replace(/'/g, '"') 
	var ratioStr = container.dataset.ratio.replace(/'/g, '"') 

	var date = JSON.parse(dateStr) 
	var carbon_ratio = JSON.parse(ratioStr) 

	var chartTooltip = document.getElementById('toolTip').getContext('2d')
	var toolTip = new Chart(chartTooltip, {
		type: 'line',
		data: {
			labels: date,
			datasets: [
				{
					label: 'Углеродный след',
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
	var el= document.getElementById('carbon_id')
	el.innerHTML += `${carbon_ratio[carbon_ratio.length - 1].toFixed(3)} кг CO₂e`
	console.log('date:', date)
	console.log('carbon_ratio:', carbon_ratio)
})


function MouseOver() {
	document.getElementById("menu_id").style.width= "4%";
	document.getElementById("chart").style.width="50px";
	document.getElementById("profile").style.width="50px";
	document.getElementById("exit").style.width="50px";
	document.getElementById("notification").style.width="50px";
	document.getElementById("settings").style.width="50px";
	document.getElementById("arrow").style.rotate="90deg";
	document.getElementById("arrow").style.width="30px";

	
}

function MouseLeave() {
	document.getElementById("menu_id").style.width= "1%";
	document.getElementById("chart").style.width="0px";
	document.getElementById("profile").style.width="0px";
	document.getElementById("exit").style.width="0px";
	document.getElementById("notification").style.width="0px";
	document.getElementById("settings").style.width="0px";
	document.getElementById("arrow").style.rotate="0deg";
	document.getElementById("arrow").style.width="20px";

	
}



