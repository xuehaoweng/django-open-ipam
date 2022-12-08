import { baseURL } from './axios.config'

export const baseAddress = ''

export const test = '/test'

export const login = '/ipam/login/'

export const updateUserInfo = '/updateUser'

export const addUserInfo = '/addUser'

export const getMenuListByRoleId = '/vue3/getMenusByRoleId'
export const getSubnetTree = '/ipam/v1/subnet_tree/'
export const PostAddressHandel = '/ipam/v1/address_handel/'
export const getinterval_schedule = '/ipam/v1/interval_schedule/'
export const getSubnetAddress = '/ipam/v1/subnet/'

export const getAllMenuByRoleId = '/getAllMenuByRoleId'

export const deleteUserById = '/deleteUserById'

export const getDepartmentList = '/vue3/getDepartmentList'

export const getNetworkDeviceList = '/api/asset_networkdevice/'

export const getCollectionPlanList = '/api/collection_plan'

export const getServerDeviceList = '/api/asset_server/'
export const getContainerList = '/api/container'
export const getcmdb_protocol_portList = '/api/cmdb_protocol_port'

export const getcmdb_accountList = '/api/cmdb_account/'
export const getasset_account_protocolList = '/api/asset_account_protocol/'
export const getauto_inventorylList = '/api/auto_inventory'
export const getauto_hostvarslList = '/api/auto_host_vars/'

export const getLoginRecordList = '/api/login_record'

export const getInterfaceUsedList = '/api/interfaceused'

export const getConfigbackupList = '/api/configbackup'

export const getPublicNetOwnerList = '/api/public_net_owner'

export const GetDptaDomainRecordList = '/api/dpta_domain_record'

export const getperiodic_taskList = '/ipam/v1/periodic_task/'

export const gettask_resultList = '/api/task_result'

export const getpublicNetFinalList = '/api/public_net_final/'

export const getpublicAlarmList = '/api/public_net_alarm'

export const getpublicResourceList = '/api/public_net_resource/'

export const get_public_net_alarm_silencesList = '/api/public_net_alarm_silences/'
export const SiteMonitor_register = '/SiteMonitor/v3/list/'

export const get_api_request_log = '/api/api_request_log'
export const get_device_account = '/asset/device_account'
export const get_device_expand = '/network/networklist/'
export const get_server_expand = '/network/serverlist/'
export const get_device_info_search = '/network/networkinfo/'
export const get_networkstatus = '/network/networkstatus/'
export const get_cmdb_idc_model = '/api/cmdb_idc_model'
export const get_cmdb_rack = '/api/cmdb_rack/'

export const getCmdbIdcList = '/api/cmdb_idc/'

export const getCmdbRoleList = '/api/cmdb_role/'

export const getVendorList = '/api/cmdb_vendor/'

export const getServerVendorList = '/api/cmdb_server_vendor/'
export const getserver_accountList = '/api/server_account'
export const getCmdbModelList = '/api/cmdb_model/'
export const getCmdbServerModelList = '/api/cmdb_server_model/'
export const getCmdbNetzoneList = '/api/cmdb_netzone/'
export const getcmdb_attributeList = '/api/cmdb_attribute/'
export const getcmdb_frameworkList = '/api/cmdb_framework/'
export const getCmdbRackList = '/api/cmdb_rack'
export const getBgbuList = '/api/bgbu/'
export const getCmdbIdcModelList = '/api/cmdb_idc_model/'
export const getCollection_planList = '/api/collection_plan'
export const getAuto_work_flowList = '/api/auto_work_flow/'

export const getFirewallList = 'v1/api/firewall_base'
export const getAddress_setList = 'v1/api/address_set/'
export const getService_setList = 'v1/api/service_set/'
export const getDnatList = 'v1/api/dnat/'
// export const getAggrePortTableList = 'automation/v3/aggrport_table/
// '
export const aggrePortTableUrl = 'vue3/aggrePortTable'

// export const getLayer3ip_tableList = 'automation/v3/layer3ip_table/'
export const layerThreeTableUrl = 'vue3/layerThreeTable'

export const getConfigBackupDetail = 'jobcenter/v3/configbakcup'

export const configBackupUrl = 'vue3/configBackup'

// export const getTaskList = 'jobcenter/v3/task_list/'
export const jobcenterTaskUrl = 'ipam/v1/jobCenter/'


export const getCategoryList = '/api/cmdb_category/'

export const getDutydayList = '/api/dutyday'

// export const getxunmiList = '/testtools/v3/iptower/'
export const ipXunMiUrl = 'vue3/ipXunmi'

export const CompareUrl = '/network/config_diff_compare/'
export const TreeList = '/network/networkresource/'

export const addDepartment = '/addDepartment'

export const getRoleList = '/getRoleList'

export const getMenuList = '/getMenuList'

export const getParentMenuList = '/getParentMenuList'

export const getTableList = '/vue3/getTableList'

export const getAutoFlow = '/api/auto_work_flow'

export const getCardList = '/getCardList'

export const getCommentList = '/getCommentList'
export const getSubnetList = '/ipam/v3/index/'
// export const getsysloginfo= '/syslog/v3/logsearch'

export const deviceLogUrl = '/vue3/deviceLog'

export const getdispach = '/jobcenter/dispatch_manage/'
export const add_crontab_schedule = '/jobcenter/add_crontab_schedule/'
export const add_interval_schedule = '/jobcenter/add_interval_schedule/'
export const del_schedule = '/jobcenter/del_schedule/'
export const get_git_config_tree = '/config_center/git_config'
export const get_alert_trend = '/alert/alarm_center/'
export const get_alert_list = '/api/alarm_center_list/'
export const dashboard_chart = '/vue3/dashboardChart'
export const public_chart = '/vue3/publicChart'
export const cmdb_chart = '/vue3/cmdbChart'
export const automation_chart = '/vue3/automationChart'
export const device_import_url = '/resources/import_assets/'
export const device_import_template = '/vue3/importTemplate'
export const alarm_shield_list = '/api/alarm_shield_list/'
export const get_topology = '/api/topology/'
export const get_flow_line = '/api/flow_view_web/'
export const alarmDeNoise = '/vue3/alarmDeNoise'
export const deviceWebSshLogin = '/vue3/deviceWebSsh'
export const serverWebSsh = '/vue3/serverWebSsh'
export const workPreserverView = '/vue3/workPreserver'
export const networkDeviceUrl = '/vue3/networkDevice'
export const api_user_plan = '/api/user_plan/'

export const get_topology_detail = '/topology/show/'
export const dnat_release = '/v1/api//dnat/'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $urlPath: Record<string, string>
  }
}
