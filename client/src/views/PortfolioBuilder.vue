<template>
    <div>
        
        <div class="flex-container">
            <div style="flex-grow: 1">
                <table class="pfTable">
                    <th>#</th>
                    <th>Stock</th>
                    <th>Amount</th>
                    <th>Price</th>
                    <th>Weight</th>
                    <tr><button @click="add">+</button></tr>
                    <tr v-for="stock in n" :key="stock">
                            <td>{{ stock }}</td>
                            <td><input v-model=name[stock]></td>
                            <td><input v-model=quantity[stock]></td>
                            <td>{{ price[stock] }}</td>
                            <td>{{ weight[stock]}}</td>
                            <td><button @click="remove(stock)">x</button></td>
                    </tr>
                    
                </table>
                    
            </div>
        </div>
    </div>
</template>

<script>
export default {
	name: 'PortfolioBuilder',
	data() {
		return {
			n: 1,
            name: [""],
            quantity : [0],
            price : [""],
            weight : [""]
		};
	},
	methods: {
        add() {
            this.n = this.n + 1;
            this.name.push("");
            this.quantity.push(0);
            this.price.push("");
            this.weight.push("");
        },
        remove(i) {
            if (this.n > 0) {
                this.n = this.n - 1;
                this.name.splice(i, 1);
                this.quantity.splice(i, 1);
                this.price.splice(i, 1);
                this.weight.splice(i, 1);
            }
        },
    },
}
</script>

<style>
.pfTable {
	margin-left: auto;
	margin-right: auto;
	border-collapse: collapse;
	padding: 0 20rem 0 0;
}

.pfTable td {
  padding: 0 0.3rem 0 0.3rem;
}

.pfTable tr:nth-child(odd) {
	background-color: #fdfcfc;
}
.pfTable tr:nth-child(even) {
	background-color: #f2f2f2;
}

.pfTable tr:hover {
	background-color: #ddd;
}

.pfTable th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align:center;
	background-color: #348bd6;
	color: white;
	width: 6rem;
}</style>