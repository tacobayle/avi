Create a specific application profile:

```
[tkg:200-100-11-11]: > show applicationprofile l4-app-preserve-client-ip
+-------------------------------+---------------------------------------------------------+
| Field                         | Value                                                   |
+-------------------------------+---------------------------------------------------------+
| uuid                          | applicationprofile-73c17a11-4f71-46d4-9ade-c27b79132c8f |
| name                          | l4-app-preserve-client-ip                               |
| type                          | APPLICATION_PROFILE_TYPE_L4                             |
| dos_rl_profile                |                                                         |
|   dos_profile                 |                                                         |
|     thresh_period             | 5 sec                                                   |
| tcp_app_profile               |                                                         |
|   proxy_protocol_enabled      | False                                                   |
|   proxy_protocol_version      | PROXY_PROTOCOL_VERSION_1                                |
|   ssl_client_certificate_mode | SSL_CLIENT_CERTIFICATE_NONE                             |
|   ftp_profile                 |                                                         |
|     deactivate_active         | False                                                   |
|     deactivate_passive        | False                                                   |
| preserve_client_ip            | True                                                    |
| preserve_client_port          | False                                                   |
| preserve_dest_ip_port         | False                                                   |
| l4_ssl_profile                |                                                         |
|   ssl_stream_idle_timeout     | 3600 sec                                                |
| tenant_ref                    | tkg                                                     |
+-------------------------------+---------------------------------------------------------+
[tkg:200-100-11-11]: >

```

Create a specific SEG with legacy HA mode:

```
[tkg:200-100-11-11]: > show serviceenginegroup Preserve-Client-ip-demo
+-----------------------------------------+---------------------------------------------------------+
| Field                                   | Value                                                   |
+-----------------------------------------+---------------------------------------------------------+
| uuid                                    | serviceenginegroup-6041b720-02bb-401a-bb6e-a14db3034831 |
| name                                    | Preserve-Client-ip-demo                                 |
| max_vs_per_se                           | 10                                                      |
| min_scaleout_per_vs                     | 2                                                       |
| max_scaleout_per_vs                     | 2                                                       |
| max_se                                  | 2                                                       |
| vcpus_per_se                            | 1                                                       |
| memory_per_se                           | 2048                                                    |
| disk_per_se                             | 15 gb                                                   |
| max_cpu_usage                           | 80 percent                                              |
| min_cpu_usage                           | 30 percent                                              |
| se_deprovision_delay                    | 120 min                                                 |
| auto_rebalance                          | False                                                   |
| se_name_prefix                          | Avi                                                     |
| vs_host_redundancy                      | True                                                    |
| vcenter_folder                          | AviSeFolder                                             |
| vcenter_datastores_include              | False                                                   |
| vcenter_datastore_mode                  | VCENTER_DATASTORE_ANY                                   |
| cpu_reserve                             | False                                                   |
| mem_reserve                             | True                                                    |
| ha_mode                                 | HA_MODE_LEGACY_ACTIVE_STANDBY                           |
| algo                                    | PLACEMENT_ALGO_DISTRIBUTED                              |
| buffer_se                               | 0                                                       |
| active_standby                          | True                                                    |
| placement_mode                          | PLACEMENT_MODE_AUTO                                     |
| se_dos_profile                          |                                                         |
|   thresh_period                         | 5 sec                                                   |
| auto_rebalance_interval                 | 300 sec                                                 |
| aggressive_failure_detection            | False                                                   |
| realtime_se_metrics                     |                                                         |
|   enabled                               | False                                                   |
|   duration                              | 30 min                                                  |
| vs_scaleout_timeout                     | 600 sec                                                 |
| vs_scalein_timeout                      | 30 sec                                                  |
| connection_memory_percentage            | 50 percent                                              |
| extra_config_multiplier                 | 0.0                                                     |
| vs_scalein_timeout_for_upgrade          | 30 sec                                                  |
| log_disksz                              | 10000 mb                                                |
| os_reserved_memory                      | 0 mb                                                    |
| hm_on_standby                           | True                                                    |
| per_app                                 | False                                                   |
| distribute_load_active_standby          | False                                                   |
| auto_redistribute_active_standby_load   | False                                                   |
| cpu_socket_affinity                     | False                                                   |
| num_flow_cores_sum_changes_to_ignore    | 8                                                       |
| least_load_core_selection               | True                                                    |
| extra_shared_config_memory              | 0 mb                                                    |
| se_tunnel_mode                          | 0                                                       |
| se_vs_hb_max_vs_in_pkt                  | 256                                                     |
| se_vs_hb_max_pkts_in_batch              | 64                                                      |
| tenant_ref                              | admin                                                   |
| cloud_ref                               | Default-Cloud                                           |
| se_thread_multiplier                    | 1                                                       |
| async_ssl                               | False                                                   |
| async_ssl_threads                       | 1                                                       |
| se_udp_encap_ipc                        | 0                                                       |
| se_tunnel_udp_port                      | 1550                                                    |
| archive_shm_limit                       | 8 gb                                                    |
| significant_log_throttle                | 100 per_second                                          |
| udf_log_throttle                        | 100 per_second                                          |
| non_significant_log_throttle            | 100 per_second                                          |
| ingress_access_mgmt                     | SG_INGRESS_ACCESS_ALL                                   |
| ingress_access_data                     | SG_INGRESS_ACCESS_ALL                                   |
| se_sb_dedicated_core                    | False                                                   |
| se_probe_port                           | 7                                                       |
| se_sb_threads                           | 1                                                       |
| ignore_rtt_threshold                    | 5000 milliseconds                                       |
| waf_mempool                             | True                                                    |
| waf_mempool_size                        | 64 kb                                                   |
| se_bandwidth_type                       | SE_BANDWIDTH_UNLIMITED                                  |
| license_type                            | LIC_CORES                                               |
| license_tier                            | ENTERPRISE                                              |
| host_gateway_monitor                    | False                                                   |
| vss_placement                           |                                                         |
|   num_subcores                          | 4                                                       |
|   core_nonaffinity                      | 2                                                       |
| flow_table_new_syn_max_entries          | 0                                                       |
| disable_csum_offloads                   | False                                                   |
| disable_tso                             | False                                                   |
| enable_hsm_priming                      | False                                                   |
| distribute_queues                       | False                                                   |
| vss_placement_enabled                   | False                                                   |
| enable_multi_lb                         | False                                                   |
| n_log_streaming_threads                 | 1                                                       |
| free_list_size                          | 1024                                                    |
| max_rules_per_lb                        | 150                                                     |
| max_public_ips_per_lb                   | 30                                                      |
| self_se_election                        | False                                                   |
| minimum_connection_memory               | 20 percent                                              |
| shm_minimum_config_memory               | 4 mb                                                    |
| heap_minimum_config_memory              | 8 mb                                                    |
| disable_se_memory_check                 | False                                                   |
| memory_for_config_update                | 15 percent                                              |
| num_dispatcher_cores                    | 0                                                       |
| ssl_preprocess_sni_hostname             | True                                                    |
| se_dpdk_pmd                             | 0                                                       |
| se_use_dpdk                             | 0                                                       |
| min_se                                  | 1                                                       |
| se_pcap_reinit_frequency                | 0 sec                                                   |
| se_pcap_reinit_threshold                | 0                                                       |
| disable_avi_securitygroups              | False                                                   |
| se_flow_probe_retries                   | 2                                                       |
| vs_switchover_timeout                   | 300 sec                                                 |
| config_debugs_on_all_cores              | False                                                   |
| accelerated_networking                  | True                                                    |
| vs_se_scaleout_ready_timeout            | 60 sec                                                  |
| vs_se_scaleout_additional_wait_time     | 0 sec                                                   |
| se_dp_hm_drops                          | 0                                                       |
| disable_flow_probes                     | False                                                   |
| dp_aggressive_hb_frequency              | 100 milliseconds                                        |
| dp_aggressive_hb_timeout_count          | 10                                                      |
| bgp_state_update_interval               | 60 sec                                                  |
| max_memory_per_mempool                  | 64 mb                                                   |
| app_cache_percent                       | 10 percent                                              |
| app_learning_memory_percent             | 0 percent                                               |
| datascript_timeout                      | 1000000                                                 |
| se_pcap_lookahead                       | False                                                   |
| enable_gratarp_permanent                | False                                                   |
| gratarp_permanent_periodicity           | 10 min                                                  |
| reboot_on_panic                         | True                                                    |
| se_flow_probe_retry_timer               | 40 milliseconds                                         |
| se_tx_batch_size                        | 64                                                      |
| se_pcap_pkt_sz                          | 69632                                                   |
| se_pcap_pkt_count                       | 0                                                       |
| distribute_vnics                        | False                                                   |
| se_dp_vnic_queue_stall_event_sleep      | 0                                                       |
| se_dp_vnic_queue_stall_timeout          | 10000                                                   |
| se_dp_vnic_queue_stall_threshold        | 2000                                                    |
| se_dp_vnic_restart_on_queue_stall_count | 3                                                       |
| se_dp_vnic_stall_se_restart_window      | 3600                                                    |
| se_pcap_qdisc_bypass                    | True                                                    |
| se_rum_sampling_nav_percent             | 1                                                       |
| se_rum_sampling_res_percent             | 100                                                     |
| se_rum_sampling_nav_interval            | 1 sec                                                   |
| se_rum_sampling_res_interval            | 2 sec                                                   |
| se_kni_burst_factor                     | 0                                                       |
| max_queues_per_vnic                     | 1                                                       |
| se_rl_prop                              |                                                         |
|   msf_num_stages                        | 1                                                       |
|   msf_stage_size                        | 16384                                                   |
| app_cache_threshold                     | 5 gb                                                    |
| core_shm_app_learning                   | False                                                   |
| core_shm_app_cache                      | False                                                   |
| pcap_tx_mode                            | PCAP_TX_AUTO                                            |
| se_dp_max_hb_version                    | 3                                                       |
| resync_time_interval                    | 65536 milliseconds                                      |
| use_hyperthreaded_cores                 | True                                                    |
| se_hyperthreaded_mode                   | SE_CPU_HT_AUTO                                          |
| compress_ip_rules_for_each_ns_subnet    | True                                                    |
| se_vnic_tx_sw_queue_size                | 256                                                     |
| se_vnic_tx_sw_queue_flush_frequency     | 0 milliseconds                                          |
| transient_shared_memory_max             | 30 percent                                              |
| labels[1]                               |                                                         |
|   key                                   | clustername                                             |
|   value                                 | tkg-cluster-workload-1                                  |
| log_malloc_failure                      | True                                                    |
| se_delayed_flow_delete                  | True                                                    |
| se_txq_threshold                        | 2048                                                    |
| se_mp_ring_retry_count                  | 500                                                     |
| dp_hb_frequency                         | 100 milliseconds                                        |
| dp_hb_timeout_count                     | 10                                                      |
| pcap_tx_ring_rd_balancing_factor        | 10 percent                                              |
| use_objsync                             | True                                                    |
| se_ip_encap_ipc                         | 0                                                       |
| se_l3_encap_ipc                         | 0                                                       |
| netlink_poller_threads                  | 2                                                       |
| netlink_sock_buf_size                   | 4 mega_bytes                                            |
| handle_per_pkt_attack                   | True                                                    |
| per_vs_admission_control                | False                                                   |
| dp_aggressive_deq_interval_msec         | 1 milliseconds                                          |
| dp_aggressive_enq_interval_msec         | 1 milliseconds                                          |
| ns_helper_deq_interval_msec             | 20 milliseconds                                         |
| dp_deq_interval_msec                    | 20 milliseconds                                         |
| dp_enq_interval_msec                    | 20 milliseconds                                         |
| send_se_ready_timeout                   | 300 seconds                                             |
| objsync_port                            | 9001                                                    |
| objsync_config                          |                                                         |
|   objsync_cpu_limit                     | 30 percent                                              |
|   objsync_reconcile_interval            | 10 sec                                                  |
|   objsync_hub_elect_interval            | 60 sec                                                  |
| vnic_dhcp_ip_check_interval             | 6 sec                                                   |
| vnic_dhcp_ip_max_retries                | 10                                                      |
| vnic_ip_delete_interval                 | 5 sec                                                   |
| vnic_probe_interval                     | 5 sec                                                   |
| vnic_rpc_retry_interval                 | 5 sec                                                   |
| vnicdb_cmd_history_size                 | 256                                                     |
| se_dp_isolation                         | False                                                   |
| se_dp_isolation_num_non_dp_cpus         | 0                                                       |
| sdb_scan_count                          | 1000                                                    |
| sdb_pipeline_size                       | 100                                                     |
| sdb_flush_interval                      | 100 milliseconds                                        |
| l7_conns_per_core                       | 16384                                                   |
| ssl_sess_cache_per_vs                   | 4096                                                    |
| l7_resvd_listen_conns_per_core          | 256                                                     |
| upstream_connpool_enable                | True                                                    |
| ngx_free_connection_stack               | False                                                   |
| http_rum_console_log                    | False                                                   |
| http_rum_min_content_length             | 64                                                      |
| upstream_connect_timeout                | 3600000 milliseconds                                    |
| upstream_send_timeout                   | 3600000 milliseconds                                    |
| upstream_read_timeout                   | 3600000 milliseconds                                    |
| downstream_send_timeout                 | 3600000 milliseconds                                    |
| lbaction_num_requests_to_dispatch       | 4                                                       |
| lbaction_rq_per_request_max_retries     | 22                                                      |
| user_defined_metric_age                 | 60 sec                                                  |
| enable_hsm_log                          | False                                                   |
| ignore_docker_mac_change                | True                                                    |
| se_dump_core_on_assert                  | False                                                   |
| se_packet_buffer_max                    | 0                                                       |
| se_dp_if_state_poll_interval            | 10                                                      |
| se_emulated_cores                       | 0                                                       |
| baremetal_dispatcher_handles_flows      | False                                                   |
| use_legacy_netlink                      | False                                                   |
| log_agent_trace_enabled                 | True                                                    |
| log_agent_debug_enabled                 | False                                                   |
| se_log_buffer_app_blocking_dequeue      | False                                                   |
| se_log_buffer_conn_blocking_dequeue     | False                                                   |
| se_log_buffer_events_blocking_dequeue   | True                                                    |
| log_agent_file_sz_debug                 | 4                                                       |
| log_agent_file_sz_conn                  | 4                                                       |
| log_agent_file_sz_appl                  | 4                                                       |
| log_agent_file_sz_event                 | 4                                                       |
| log_agent_min_storage_per_vs            | 10                                                      |
| log_agent_max_storage_ignore_percent    | 20.0                                                    |
| log_agent_max_storage_excess_percent    | 110                                                     |
| se_dp_log_nf_enqueue_percent            | 70                                                      |
| se_dp_log_udf_enqueue_percent           | 90                                                      |
| log_agent_compress_logs                 | True                                                    |
| log_agent_sleep_interval                | 10 milliseconds                                         |
| log_agent_unknown_vs_timer              | 1800 sec                                                |
| log_agent_max_concurrent_rsync          | 1024                                                    |
| log_agent_log_storage_min_sz            | 1024 mb                                                 |
| log_message_max_file_list_size          | 64                                                      |
| bgp_peer_monitor_failover_enabled       | False                                                   |
| max_skb_frags                           | 17                                                      |
| hybrid_rss_mode                         | False                                                   |
| num_dispatcher_queues                   | 1                                                       |
| dpdk_gro_timeout_interval               | 50 microseconds                                         |
| se_time_tracker_props                   |                                                         |
|   ingress_threshold                     | 20 milliseconds                                         |
|   egress_threshold                      | 20 milliseconds                                         |
|   ingress_audit_mode                    | SE_TT_AUDIT_OFF                                         |
|   egress_audit_mode                     | SE_TT_AUDIT_OFF                                         |
|   event_gen_window                      | 300 seconds                                             |
| grpc_channel_connect_timeout            | 15                                                      |
| ntp_sync_fail_event                     | False                                                   |
| ntp_sync_status_interval                | 0 sec                                                   |
| use_dp_util_for_scaleout                | False                                                   |
| replay_vrf_routes_interval              | 1000 milliseconds                                       |
+-----------------------------------------+---------------------------------------------------------+
```

Create a specific network service associated with the previous SE group created (floating_intf_ip is a list which contains the floating IPs for the external side and internal side, order does not matter):

```
[tkg:200-100-11-11]: > show networkservice actstndby
+--------------------------------+-----------------------------------------------------+
| Field                          | Value                                               |
+--------------------------------+-----------------------------------------------------+
| uuid                           | networkservice-35019c01-f9f0-48b3-bef0-9bf41f044391 |
| name                           | actstndby                                           |
| se_group_ref                   | Preserve-Client-ip-demo                             |
| vrf_ref                        | global                                              |
| service_type                   | ROUTING_SERVICE                                     |
| routing_service                |                                                     |
|   enable_routing               | True                                                |
|   routing_by_linux_ipstack     | False                                               |
|   floating_intf_ip[1]          | 172.16.120.200                                      |
|   floating_intf_ip[2]          | 200.100.12.222                                      |
|   enable_vmac                  | False                                               |
|   enable_vip_on_all_interfaces | True                                                |
|   advertise_backend_networks   | False                                               |
|   graceful_restart             | False                                               |
|   enable_auto_gateway          | True                                                |
| tenant_ref                     | admin                                               |
| cloud_ref                      | Default-Cloud                                       |
+--------------------------------+-----------------------------------------------------+
```

Create a Virtual service associated with SE group and application profile:

```
[tkg:200-100-11-11]: > show virtualservice tkg-cluster-workload-1--default-sctp
+------------------------------------+----------------------------------------------------------------------------------+
| Field                              | Value                                                                            |
+------------------------------------+----------------------------------------------------------------------------------+
| uuid                               | virtualservice-4a1e0633-63f2-496a-a01d-2a13468c78a4                              |
| name                               | tkg-cluster-workload-1--default-sctp                                             |
| enabled                            | True                                                                             |
| services[1]                        |                                                                                  |
|   port                             | 3861                                                                             |
|   enable_ssl                       | False                                                                            |
|   port_range_end                   | 3861                                                                             |
|   enable_http2                     | False                                                                            |
|   horizon_internal_ports           | False                                                                            |
|   is_active_ftp_data_port          | False                                                                            |
| application_profile_ref            | l4-app-preserve-client-ip                                                        |
| network_profile_ref                | System-SCTP-Proxy                                                                |
| se_group_ref                       | Preserve-Client-ip-demo                                                          |
| network_security_policy_ref        | tkg-cluster-workload-1--default-sctp-NetworkSecurityPolicy                       |
| http_policies[1]                   |                                                                                  |
|   index                            | 11                                                                               |
|   http_policy_set_ref              | tkg-cluster-workload-1--default-sctp-HTTPPolicySet-0                             |
| analytics_policy                   |                                                                                  |
|   full_client_logs                 |                                                                                  |
|     enabled                        | True                                                                             |
|     duration                       | 0 min                                                                            |
|     throttle                       | 10 per_second                                                                    |
|   client_insights                  | NO_INSIGHTS                                                                      |
|   all_headers                      | False                                                                            |
|   metrics_realtime_update          |                                                                                  |
|     enabled                        | False                                                                            |
|     duration                       | 30 min                                                                           |
|   udf_log_throttle                 | 10 per_second                                                                    |
|   significant_log_throttle         | 10 per_second                                                                    |
|   learning_log_policy              |                                                                                  |
|     enabled                        | False                                                                            |
| vrf_context_ref                    | global                                                                           |
| enable_autogw                      | True                                                                             |
| analytics_profile_ref              | System-Analytics-Profile                                                         |
| weight                             | 1                                                                                |
| delay_fairness                     | False                                                                            |
| max_cps_per_client                 | 0                                                                                |
| limit_doser                        | False                                                                            |
| type                               | VS_TYPE_NORMAL                                                                   |
| cloud_type                         | CLOUD_VCENTER                                                                    |
| use_bridge_ip_as_vip               | False                                                                            |
| flow_dist                          | LOAD_AWARE                                                                       |
| ign_pool_net_reach                 | False                                                                            |
| ssl_sess_cache_avg_size            | 1024                                                                             |
| remove_listening_port_on_vs_down   | True                                                                             |
| close_client_conn_on_config_update | False                                                                            |
| bulk_sync_kvcache                  | False                                                                            |
| advertise_down_vs                  | False                                                                            |
| tenant_ref                         | tkg                                                                              |
| cloud_ref                          | Default-Cloud                                                                    |
| east_west_placement                | False                                                                            |
| scaleout_ecmp                      | False                                                                            |
| created_by                         | ako-tkg-cluster-workload-1                                                       |
| cloud_config_cksum                 | 3684237708                                                                       |
| enable_rhi                         | True                                                                             |
| active_standby_se_tag              | ACTIVE_STANDBY_SE_1                                                              |
| flow_label_type                    | NO_LABEL                                                                         |
| service_metadata                   | {"namespace_ingress_name":null,"ingress_name":"","namespace":"","hostnames":["sc |
|                                    | tp.default.avi-telco.com"],"namespace_svc_name":["default/sctp"],"crd_status":{" |
|                                    | type":"","value":"","status":""},"pool_ratio":0,"passthrough_parent_ref":"","pas |
|                                    | sthrough_child_ref":"","gateway":"","insecureedgetermallow":false,"is_mci_ingres |
|                                    | s":false}                                                                        |
| vsvip_ref                          | tkg-cluster-workload-1--default-sctp                                             |
| use_vip_as_snat                    | False                                                                            |
| error_page_profile_ref             | Custom-Error-Page-Profile                                                        |
| l4_policies[1]                     |                                                                                  |
|   index                            | 0                                                                                |
|   l4_policy_set_ref                | tkg-cluster-workload-1--default-sctp                                             |
| traffic_enabled                    | True                                                                             |
| markers[1]                         |                                                                                  |
|   key                              | clustername                                                                      |
|   values[1]                        | tkg-cluster-workload-1                                                           |
| markers[2]                         |                                                                                  |
|   key                              | Namespace                                                                        |
|   values[1]                        | default                                                                          |
| markers[3]                         |                                                                                  |
|   key                              | ServiceName                                                                      |
|   values[1]                        | sctp                                                                             |
| allow_invalid_client_cert          | False                                                                            |
| vh_type                            | VS_TYPE_VH_SNI                                                                   |
+------------------------------------+----------------------------------------------------------------------------------+
[tkg:200-100-11-11]: >
```
