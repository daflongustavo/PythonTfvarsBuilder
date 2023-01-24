def resolves_project_type_1(path_to_download_in_repo, waf_log_type, ip_block):
    path_to_download_in_repo += "/LambdaAPIGateway"
    if waf_log_type == 1:
        path_to_download_in_repo += "/NoWAFCentralizedLogs"
    if waf_log_type == 2:
        path_to_download_in_repo += "/NoWAFCloudWatchLogs"
    if waf_log_type == 3:
        path_to_download_in_repo += "/NoWAFNoLogs"
    if waf_log_type == 4:
        path_to_download_in_repo += "/WAFCentralizedLogs"
        if ip_block:
            path_to_download_in_repo += "/WAFCentralizedLogsIPBlock"
        else:
            path_to_download_in_repo += "/WAFCentralizedLogsNoIPBlock"
    if waf_log_type == 5:
        path_to_download_in_repo += "/WAFCloudWatchLogs"
        if ip_block:
            path_to_download_in_repo += "/WAFCloudWatchLogsIPBlock"
        else:
            path_to_download_in_repo += "/WAFCloudWatchLogsIPBlock"
    if waf_log_type == 6:
        path_to_download_in_repo += "/WAFNoLogs"
        if ip_block:
            path_to_download_in_repo += "/WAFNoLogsIPBlock"
        else:
            path_to_download_in_repo += "/WAFNoLogsNoIPBlock"

    return path_to_download_in_repo
