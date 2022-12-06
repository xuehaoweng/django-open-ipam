<template>
  <div class="action-items-wrapper">

    <span class="action-item" @click="duty_show=true">今日值班:{{ today_info }}</span>
    <span class="action-item" @click="duty_show=true">明日值班:{{ tomorrow_info }}</span>
    <!--网关设备搜索-->
    <n-input style="width:100px" v-model:value="content" placeholder="" @keyup.native.enter="GatewayOnSearch"/>

    <span v-if="state.actionItem.showSearch" class="action-item" @click="show_search_show = true">
      <n-icon size="18">
        <SearchIcon/>
      </n-icon>
    </span>

    <span v-if="state.actionItem.showRefresh" class="action-item" @click="onRefrehRoute">
      <n-icon size="18">
        <RefreshIcon/>
      </n-icon>
    </span>
    <span
        v-if="state.actionItem.showFullScreen && state.device !== 'mobile'"
        class="action-item"
        @click="onScreenFull"
    >
      <n-icon size="18">
        <ExpandIcon/>
      </n-icon>
    </span>
    <span class="action-item" @click="onShowSetting">
      <n-icon size="18">
        <SettingIcon/>
      </n-icon>
    </span>

    <SearchContent ref="searchContentRef"/>

    <Setting ref="settingRef"/>


    <n-modal v-model:show="duty_show"
             preset="dialog"
             header-style="padding: 10px 20px"
             title="运维值班"
             :style="{ height: '900px',width:'1300px' }"
    >
      <n-grid x-gap="12" :cols="1">
        <n-gi>
          <DutyChart ref="dutyChart"/>
        </n-gi>
      </n-grid>
    </n-modal>
    <n-modal v-model:show="show_search_show"
             preset="dialog"
             header-style="padding: 10px 20px"
             title="全局搜索"
             :style="{ height: '600px',width:'1000px' }"
    >
      <!--      <n-grid x-gap="12" :cols="1">-->

      <!--        <n-gi>-->
      <!--          <DutyChart ref="dutyChart"/>-->
      <!--        </n-gi>-->
      <!--      </n-grid>-->
      <n-space vertical>
        <n-button>寻觅系统</n-button>
        <n-button>DNAT</n-button>
        <n-button>SNAT</n-button>
      </n-space>
    </n-modal>

  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { getDutydayList, get_device_info_search } from '@/api/url'
import { useMessage } from 'naive-ui'
import screenfull from 'screenfull'
import { useRoute, useRouter } from 'vue-router'
import { useLayoutStore } from '../../components/index'
import { SearchContentType } from '@/types/components'
import {
  SettingsOutline as SettingIcon,
  SearchOutline as SearchIcon,
  Expand as ExpandIcon,
  NotificationsOutline as NotificationsIcon,
  RefreshOutline as RefreshIcon,
} from '@vicons/ionicons5'
import useGet from '@/hooks/useGet'
import router from '@/router'
import DutyChart from '@/views/index/components/chart/DutyChart.vue'

export default defineComponent({
  name: 'ActionItems',
  components: {
    SearchIcon,
    SettingIcon,
    ExpandIcon,
    NotificationsIcon,
    RefreshIcon,
    DutyChart,
  },
  setup() {
    const duty_show = ref(false)
    const show_search_show = ref(false)
    const content = ref('')
    const searchContentRef = ref<SearchContentType>()
    const showSearchContent = ref(false)
    const searchContent = ref('')
    const settingRef = ref()
    const badgeValue = ref(3)
    const store = useLayoutStore()
    const message = useMessage()
    const router = useRouter()
    const route = useRoute()
    const get = useGet()
    const today_info = ref('')
    const tomorrow_info = ref('')

    function onShowSearch() {
      searchContentRef.value?.onShow()
    }

    function onScreenFull() {
      if (!screenfull.isEnabled) {
        message.error('当前浏览器不支持全屏操作')
        return false
      }
      screenfull.toggle()
    }

    function onRefrehRoute() {
      router.replace({ path: '/redirect' + route.path })
    }

    function onShowSetting() {
      settingRef.value.openDrawer()
    }

    function get_duty_day() {
      //getDutydayList
      get({
        url: getDutydayList,
        data: () => {
          return {
            limit: 1000,
            start: 0,
          }
        },
      })
          .then((res) => {
            // console.log(res)
            const today = get_day_time(0)
            const tomorrow = get_day_time(1)
            // console.log('tomorrow_info.value', tomorrow, tomorrow_info.value)
            today_info.value = res.results.filter((ele) => {
              return ele['date'] === today
            })[0]['dutyuser_user'] + res.results.filter((ele) => {
              return ele['date'] === today
            })[0]['user_tel']
            // console.log('today_info.value', today, today_info.value)
            tomorrow_info.value = res.results.filter((ele) => {
              return ele['date'] === tomorrow
            })[0]['dutyuser_user'] + res.results.filter((ele) => {
              return ele['date'] === tomorrow
            })[0]['user_tel']

            // let duty_array = []
            // duty_array.length = 0


          })
    }

    function get_day_time(num) {
      var date = new Date()
      var year = date.getFullYear()
      var month = date.getMonth() + 1
      var day = date.getDate() + num
      var time = ''
      if (month < 10 && day < 10) {
        time = year + '-0' + month + '-0' + day
      }
      if (month < 10 && day >= 10) {
        time = year + '-0' + month + '-' + day
      }

      return time
    }

    function GatewayOnSearch() {
      if (!content.value) {
        return
      }
      // content.value = ''
      // show.value = false
      // var exp_ipaddr =
      //     /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.*$/
      // var reg_ipaddr = content.value.match(exp_ipaddr)
      // if (reg_ipaddr != null) {
      //   message.info('IP地址合法')
      sessionStorage.setItem('gateway_key', content.value)
      get({
        url: get_device_info_search,
        data: () => {
          return {
            gateway_key: content.value,
          }
        },
      }).then((res) => {
        if (res.results) {
          const hostlist = sessionStorage.getItem('hostlist')
          if (hostlist) {
            sessionStorage.removeItem('hostlist')
            sessionStorage.setItem('last_path', route.path)
          }


          sessionStorage.setItem('hostlist', res.results)
          router.push('/cmdb/network_device')
        } else {
          message.error('检索无数据')
          sessionStorage.removeItem('hostlist')
        }

      })
      // } else {
      //   message.error('IP地址不合法')
      // }
      console.log('content.value', content.value)
      // window.open('https://www.baidu.com/s?wd=' + content.value)

    }

    // onMounted(get_duty_day)
    return {
      duty_show,
      show_search_show,
      tomorrow_info,
      today_info,
      get_duty_day,
      get_day_time,
      searchContentRef,
      settingRef,
      showSearchContent,
      searchContent,
      badgeValue,
      state: store.state,
      onShowSearch,
      onScreenFull,
      onRefrehRoute,
      onShowSetting,
      content,
      GatewayOnSearch,
    }
  },
})
</script>

<style lang="scss" scoped>
.action-items-wrapper {
  position: relative;
  height: 100%;
  display: flex;
  align-items: center;
  z-index: 1;

  .action-item {
    min-width: 40px;
    display: flex;
    align-items: center;
    padding-right: 10px;

    &:hover {
      cursor: pointer;
      color: var(--primary-color-hover);
    }
  }

  .badge-action-item {
    cursor: pointer;
    margin-right: 30px;
  }
}
</style>
<style lang="scss" scoped>
:deep(.n-input .n-input__border, .n-input .n-input__state-border) {
  border: none;
  border-bottom: 1px solid currentColor;
}

:deep(.el-input__inner) {
  border: none !important;
  height: 35px;
  line-height: 35px;
  color: currentColor !important;
  background-color: transparent !important;
}
</style>
