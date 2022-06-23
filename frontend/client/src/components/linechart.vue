<template>
	<h1>Line Chart</h1>
	<v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { LineChart } from 'echarts/charts'
import { GridComponent } from 'echarts/components'
import VChart from "vue-echarts";
import { ref, defineComponent } from "vue";

use([
	CanvasRenderer,
	LineChart,
	GridComponent
]);


export default defineComponent({
	name: 'LineChart',
	components: {
		VChart,
	},

	setup() {
		const option = ref({
			xAxis: {
				type: 'category',
				data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
			},
			yAxis: {
				type: 'value'
			},
			series: [
				{
					data: [150, 230, 224, 218, 135, 147, 260],
					type: 'line'
				}
			]
		});

		return { option };
	}
});



</script>

<style scoped>
.chart {
	height: 800px;
	width: 100%;
}
</style>