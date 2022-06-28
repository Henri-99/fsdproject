<template>
	<v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { LineChart } from 'echarts/charts'
import { GridComponent } from 'echarts/components'
import VChart from "vue-echarts";
import { ref, defineComponent, watchEffect } from "vue";

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
	props: {
		data: {},
	},
	setup(props) {
		const option = ref({
			tooltip: {
				trigger: 'axis',
				formatter: function (params) {
					params = params[0];
					var date = new Date(params.name);
					return (
						date.getDate() +
						'/' +
						(date.getMonth() + 1) +
						'/' +
						date.getFullYear() +
						' : ' +
						params.value[1]
					);
				},
				axisPointer: {
					animation: false
				}
			},
			xAxis: {
				type: 'time',
				splitLine: {
					show: false
				}
			},
			yAxis: {
				type: 'value',
				splitLine: {
					show: false
				}
			},
			series: [
				{
					name: 'Stock Data',
					type: 'line',
					showSymbol: false,
					data: props.data
				}
			]
		})

		watchEffect(
			() =>
			(option.value.series = [
				{
					name: 'Data',
					type: 'line',
					showSymbol: false,
					data: props.data
				},
			]),
			console.log(props.data), 
		);

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