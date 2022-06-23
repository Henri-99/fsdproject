<template>
	<div>
		<select v-model="indexCode">
			<option disabled value="">Select an Index</option>
			<option v-for="index in indices" :key="index">{{ index }}</option>
		</select>
	</div>

	<div class="flex-container">
		<div style="flex-grow: 1">
			<table class="stocklist" v-if="indexCode">
				<tr>
					<th>Stock</th>
					<th>Weight</th>
				</tr>
				<tr v-for="stock in msg" :key="stock">
					<td>{{ stock.name }} </td>
					<td>{{ (stock.value * 100).toFixed(2) }} % </td>
				</tr>
			</table>
		</div>


		<div style="flex-grow: 2" v-if="res">
			<PieChart :key="indexCode" :indexName="indexCode" :data="msg" />
		</div>

	</div>
</template>

<script>
import axios from 'axios';
import PieChart from '../components/charts.vue';

export default {
	name: 'PingTest',
	components: {
		PieChart,
	},
	data() {
		return {
			msg: '',
			indexCode: '',
			res: {},
		};
	},
	methods: {
		getMessage() {
			const path = 'http://localhost:5000/ping?index='.concat(this.indexCode);
			axios.get(path)
				.then((res) => {
					this.msg = res.data;
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
		},
	},
	watch: {
		indexCode() {
			this.getMessage();
		}
	},
	created() {
		this.indices = ["ALSI", "FLED", "LRGC", "MIDC", "SMLC", "TOPI", "RESI", "FINI", "INDI", "PCAP", "SAPY", "ALTI"];
	},

};
</script>

<style>
.stocklist {
	margin-left: auto;
	margin-right: 0;
	border-collapse: collapse;
}

.stocklist td,
.stocklist th {
	border: 1px solid #ddd;
	padding: 3px 10px 3px 10px;
}

.stocklist tr:nth-child(even) {
	background-color: #f2f2f2;
}

.stocklist tr:hover {
	background-color: #ddd;
}

.stocklist th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: left;
	background-color: #348bd6;
	color: white;
}

.flex-container {
    display: flex;
}

</style>