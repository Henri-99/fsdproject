<template>
	<v-chart class="piechart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
	TooltipComponent
} from "echarts/components";
import VChart from "vue-echarts";
import { ref, defineComponent, watchEffect } from "vue";

use([
	CanvasRenderer,
	PieChart,
	TooltipComponent
]);


export default defineComponent({
	name: 'PieChart',
	components: {
		VChart
	},
	props: {
		indexName: String,
		data: {},
	},
	setup(props) {
		const option = ref({
			tooltip: {
				trigger: "item",
				formatter: "{b} : {d}%"
			},
			series: [
				{
					name: props.indexName,
					type: "pie",
					radius: "80%",
					center: ["50%", "50%"],
					data: props.data,
					emphasis: {
						itemStyle: {
							shadowBlur: 10,
							shadowOffsetX: 0,
							shadowColor: "rgba(0, 0, 0, 0.5)"
						}
					}
				}
			]
		})
		watchEffect(() => {
			console.log(props.data[1]);
			option.value.series = [
				{
					name: props.indexName,
					type: "pie",
					radius: "80%",
					center: ["50%", "50%"],
					data: props.data,
					emphasis: {
						itemStyle: {
							shadowBlur: 10,
							shadowOffsetX: 0,
							shadowColor: "rgba(0, 0, 0, 0.5)"
						}
					}
				}
			]
		})
		// console.log("Pie Chart Updated");
		// console.log(props.indexName)
		// console.log(props.data[1])
		return { option };
	}


});



</script>

<style scoped>
.piechart {
	height: 50vw;
	margin: 10rem 5rem 5rem 5rem;
}
</style>