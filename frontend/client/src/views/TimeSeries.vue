<template>

	<h2>Line Chart</h2>
	<h3>x-axis: Date Period (user specified)</h3>
	<h3>y-axis: Share (user specified)</h3>
	<h3>y-axis: Index (user specified)</h3>
	
	<LineChart />

</template>

<script>

import LineChart from '../components/linechart.vue';

export default {
	name: 'TimeSeries',
	components: {
		LineChart
	},
};
</script>

<style>
.center {
	margin-left: auto;
	margin-right: auto;
	border-collapse: collapse;
}

.center td,
.center th {
	border: 1px solid #ddd;
	padding: 3px 10px 3px 10px;
}

.center tr:nth-child(even) {
	background-color: #f2f2f2;
}

.center tr:hover {
	background-color: #ddd;
}

.center th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: left;
	background-color: #348bd6;
	color: white;
}

.flex-container {
    display: flex;
}
.flex-child {
    flex: 1;
}  
</style>