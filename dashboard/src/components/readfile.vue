<script>
      import json from './data/data.json'
      export default{
          data(){
              return{
                  myJson: json
              }
          }
      }
</script>

<template>
    <div>
        <div v-for="data in myJson">{{data}}</div>
    </div>
</template>