<template>
    <div class="about">
      <el-button @click="handletransferData">随机袋数据</el-button>
      <el-button @click="handletransferDataC">带确定数据</el-button>
      <el-button @click="handletransferDataE">带空数据</el-button>
      <el-button @click="handletransferDataA">带全数据</el-button>
      <lzl-dialog :dataorg="data" :visible="visible" @handleconfirm="handleconfirm" @handleCancel="visible=false"></lzl-dialog>
    </div>
</template>

<script>
import lzlDialog from './lzlDialog.vue'
export default {
    components: {
        lzlDialog
    },
    data() {
        return {
            data: [],
            visible: false
        };
    },
    methods: {
        handleconfirm(data) {
            alert(data)
        },
        handletransferData() {
            var arr=[['9'],['1'],['2'],['1','2']]
            this.data = arr[Math.floor(Math.random()*4)]
            this.visible  = true
        },
        handletransferDataC() {
            // var arr=[['9'],['1'],['2'],['1','2']]
            this.data = ['2']
            this.visible  = true
        },
        handletransferDataE() {
            // var arr=[['9'],['1'],['2'],['1','2']]
            this.data = []
            this.visible  = true
        },
        handletransferDataA() {
            // var arr=[['9'],['1'],['2'],['1','2']]
            this.data = ['1','2','3']
            this.visible  = true
        }
        
    }
};
</script>

<style lang="scss" scoped>
$color: red;
.about {
    border: 1px solid $color;
    &::before {
        content: "";
    }
}
</style>