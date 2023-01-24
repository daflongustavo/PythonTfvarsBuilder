import requests
def builds_tfvars_for_sca(base_networking, project_type, waf_log_type, ip_block):
    path_to_download_in_repo = "https://api.github.com/repos/7clouds-serverless-solutions/sca-tf-templates/contents" \
                               "/tfvars_templates"
    response = requests.get(path_to_download_in_repo)

    if response.status_code == 200:
        contents = response.json()
        for item in contents:
            print(f"Download successful: \n {item['name']}")

    else:
        print(f"Error: {response.status_code}")

    if base_networking:
        path_to_download_in_repo += "/BaseNetworking"

        if project_type == 1:
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
                    path_to_download_in_repo += "/WAFCentralizedLogsIPBlock"
                else:
                    path_to_download_in_repo += "/WAFCentralizedLogsNoIPBlock"
            if waf_log_type == 6:
                path_to_download_in_repo += "/WAFNoLogs"
                if ip_block:
                    path_to_download_in_repo += "/WAFCentralizedLogsIPBlock"
                else:
                    path_to_download_in_repo += "/WAFCentralizedLogsNoIPBlock"


builds_tfvars_for_sca(base_networking=True, project_type=1, waf_log_type=1, ip_block=True)
