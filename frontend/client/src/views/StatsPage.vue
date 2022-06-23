<template>
	<div>
		<select v-model="indexCode">
			<option disabled value="">Select an Index</option>
			<option v-for="index in indices" :key="index">{{ index }}</option>
		</select>
	</div>
	<div>
		<select v-model="mktIndex">
			<option disabled value="">Select a Market Index</option>
			<option v-for="index in mktIndices" :key="index">{{ index }}</option>
		</select>
	</div>
	<div>
		<select v-model="stat">
			<option disabled value="">Select a Statistic</option>
			<option v-for="stat in stats" :key="stat">{{ stat }}</option>
		</select>
	</div>

	<div class="flex-container">
		<div style="flex-grow: 1">
			<table class="stocklist" v-if="indexCode">
				<tr v-for="stock in msg" :key="stock">
					<!-- <td v-for="col in stock" :key="col"> {{ col.toFixed(5) }} </td> -->
					{{ stock }}
				</tr>
			</table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'StatsPage',
	data() {
		return {
			msg: '',
			indexCode: '',
			mktIndex : '',
			stat : '',
			res: {},
		};
	},
	methods: {
		getMessage() {
			const path = 'http://localhost:5000/stat?index='.concat(this.indexCode, '&market=', this.mktIndex, '&s=', this.stat);
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
			if (this.mktIndex !== '' && this.stat !== '') {
				this.getMessage();
			}
		},
		mktIndex() {
			if (this.indexCode !== '' && this.stat !== '') {
				this.getMessage();
			}
		},
		stat() {
			if (this.mktIndex !== '' && this.indexCode !== '') {
				this.getMessage();
			}
		},
	},
	created() {
		this.indices = ["ALSI", "FLED", "LRGC", "MIDC", "SMLC", "TOPI", "RESI", "FINI", "INDI", "PCAP", "SAPY", "ALTI"];
		this.mktIndices = ["J203", "J200", "J250", "J257", "J258"]
		this.stats = ['beta', 'specVols', 'pfBeta', 'sysCov', 'pfSysVol', 'specCov', 'pfSpecVol', 'totCov', 'pfVol', 'corrMat']
	},

};
</script>

<style>
.stocklist {
	margin-left: auto;
	margin-right: auto;
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