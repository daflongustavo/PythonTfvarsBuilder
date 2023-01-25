def resolves_project_type(repo_download_path, waf_log_type, ip_block):
    if waf_log_type == 1:
        repo_download_path += "/NoWAFCentralizedLogs"
    if waf_log_type == 2:
        repo_download_path += "/NoWAFCloudWatchLogs"
    if waf_log_type == 3:
        repo_download_path += "/NoWAFNoLogs"
    if waf_log_type == 4:
        repo_download_path += "/WAFCentralizedLogs"
        if ip_block:
            repo_download_path += "/WAFCentralizedLogsIPBlock"
        else:
            repo_download_path += "/WAFCentralizedLogsNoIPBlock"
    if waf_log_type == 5:
        repo_download_path += "/WAFCloudWatchLogs"
        if ip_block:
            repo_download_path += "/WAFCloudWatchLogsIPBlock"
        else:
            repo_download_path += "/WAFCloudWatchLogsIPBlock"
    if waf_log_type == 6:
        repo_download_path += "/WAFNoLogs"
        if ip_block:
            repo_download_path += "/WAFNoLogsIPBlock"
        else:
            repo_download_path += "/WAFNoLogsNoIPBlock"

    return repo_download_path

