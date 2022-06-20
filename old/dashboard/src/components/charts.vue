<template>
	<h1>Bar Chart</h1>
	<v-chart class="chart" :option="option" />
</template>

<script>
import NavBarVue from './NavBar.vue'
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
	TitleComponent,
	TooltipComponent,
	LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { ref, defineComponent } from "vue";

use([
	CanvasRenderer,
	PieChart,
	TitleComponent,
	TooltipComponent,
	LegendComponent
]);


export default defineComponent({
	name: 'charts',
	components: {
		VChart,
		NavBarVue
	},

	setup() {
		const option = ref({
			title: {
				text: "ALTI (Sep 2017)",
				left: "center"
			},
			tooltip: {
				trigger: "item",
				formatter: "{b} : {d}%"
			},
			legend: {
				orient: "vertical",
				left: "left",
				data: ["ACE", "ACG", "ADW", "ALH", "ANS", "AVL", "BSS", "BUC", "GAM", "GBI", "GLI", "HET", "IHL", "ILE", "ISA", "JBL", "KBO", "MAP", "NFP", "NUT", "OAS", "PEM", "PSV", "REN", "SVB", "UPL", "VUN", "WEA"]
			},
			series: [
				{
					name: "ALTI",
					type: "pie",
					radius: "55%",
					center: ["50%", "60%"],
					data: [
						{ value: 0.007, name: "ACE" },
						{ value: 0.06, name: "ACG" },
						{ value: 0.001, name: "ADW" },
						{ value: 0.015, name: "ALH" },
						{ value: 0.033, name: "ANS" },
						{ value: 0.016, name: "AVL" },
						{ value: 0.014, name: "BSS" },
						{ value: 0.017, name: "BUC" },
						{ value: 0.012, name: "GAM" },
						{ value: 0.004, name: "GBI" },
						{ value: 0.036, name: "GLI" },
						{ value: 0.172, name: "HET" },
						{ value: 0.063, name: "IHL" },
						{ value: 0.002, name: "ILE" },
						{ value: 0.018, name: "ISA" },
						{ value: 0.052, name: "JBL" },
						{ value: 0.028, name: "KBO" },
						{ value: 0.008, name: "MAP" },
						{ value: 0.195, name: "NFP" },
						{ value: 0.003, name: "NUT" },
						{ value: 0.072, name: "OAS" },
						{ value: 0.013, name: "PEM" },
						{ value: 0.008, name: "PSV" },
						{ value: 0.053, name: "REN" },
						{ value: 0.005, name: "SVB" },
						{ value: 0.065, name: "UPL" },
						{ value: 0.03, name: "VUN" },
						{ value: 0.001, name: "WEA" }
					],
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

		return { option };
	}
});



</script>

<style scoped>
.chart {
	height: 800px;
}
</style>