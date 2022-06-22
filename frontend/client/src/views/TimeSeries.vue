<template>

	<h2>Line Chart</h2>
	<h3>x-axis: Date Period (user specified)</h3>
	<h3>y-axis: Share (user specified)</h3>
	<h3>y-axis: Index (user specified)</h3>
	
	<div>
		<select v-model="indexCode">
			<option disabled value="">Select an Index Code</option>
			<option v-for="index in indices" :key="index">{{ index }}</option>
		</select>
	</div>

	<div class="flex-container">
		<div class="flex-child">

			<h2>{{ indexCode }}</h2>
			<table class="center" v-if="msg">
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


		<div class="flex-child" v-if="msg">
			<PieChart :key="indexCode" :indexName="indexCode" :data="msg" />
		</div>

	</div>
</template>

<script>
import axios from 'axios';
import PieChart from '../components/charts.vue';

export default {
	name: 'TimeSeries',
	components: {
		PieChart,
	},
	data() {
		return {
			msg: '',
			indexCode: '',
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