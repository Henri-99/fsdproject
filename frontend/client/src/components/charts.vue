<template>
	<v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
	TitleComponent,
	TooltipComponent
} from "echarts/components";
import VChart from "vue-echarts";
import { ref, defineComponent } from "vue";

use([
	CanvasRenderer,
	PieChart,
	TitleComponent,
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
			title: {
				text: props.indexName,
				left: "center"
			},
			tooltip: {
				trigger: "item",
				formatter: "{b} : {d}%"
			},
			// legend: {
			// 	orient: "vertical",
			// 	left: "left",
			// 	data: ["ACE", "ACG", "ADW", "ALH", "ANS", "AVL", "BSS", "BUC", "GAM", "GBI", "GLI", "HET", "IHL", "ILE", "ISA", "JBL", "KBO", "MAP", "NFP", "NUT", "OAS", "PEM", "PSV", "REN", "SVB", "UPL", "VUN", "WEA"]
			// },
			series: [
				{
					name: props.indexName,
					type: "pie",
					radius: "55%",
					center: ["50%", "60%"],
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
		});
		console.log("Pie'd");
		return { option };
	}
});



</script>

<style scoped>
.chart {
	height: 800px;
	width: 100%
}
</style>