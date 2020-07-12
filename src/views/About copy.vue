<template>
  <div class="about">
    sdf1
    <el-button type="primary" @click="add">添加</el-button>
    <el-button @click="del">删除</el-button>
    <el-form :model="list" :rules="rules">
      <el-form-item  prop="title" label="项目名">
        <el-input v-model="list.title">sdf</el-input>
      </el-form-item>
      <el-form-item  prop="id" label="所属项目">
        <el-input v-model="list.id">sdf</el-input>
      </el-form-item>

      <el-form-item v-for="(item2, index2) in list.detail" :key="index2" >
        <el-checkbox-group v-model="item2.group">
          <el-checkbox v-for="(item, index) in dictInfo" :key="index" :value="item.type" :label="item.name"></el-checkbox>
        </el-checkbox-group>
          <div style="margin-top: 20px">
            <el-input v-model="item2.cardId"></el-input>
            <el-input v-model="item2.range"></el-input>
          </div>
        
      </el-form-item>


    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rules:{
        title:[{
          required: true, message:'不为空', trigger:'blur'
        }]
      },
      list:{
        title:'',
        id:'',
        detail: [{
          cardid: '',
          range:'',
          group:[]

        }]
      },
      dictInfo : [{
        type:'00',
        name: '单选'
      },{
        type:'01',
        name: '多选'
      },{
        type:'02',
        name: '不定项'
      },{
        type:'03',
        name: '简答'
      },{
        type:'04',
        name: '编程'
      },{
        type:'05',
        name: '数据库'
      },]
    }
  },
  methods: {
    add() {
      this.list.detail.push({
        cardId: '',
        range: '',
        group: []
      })
      
    },
    del() {
  this.list.detail.pop()      
    }
  }
}
</script>

<style lang="scss" scoped>
$color : red;
.about {
  border: 1px solid $color;
  &::before {
    content: '';
  }
}
</style>