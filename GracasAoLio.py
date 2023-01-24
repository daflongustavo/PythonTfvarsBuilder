import requests
from pathlib import Path
import shutil

from ProjectTypesResolvers import resolves_project_type_1


def creates_new_directory_tfvars():
    tfvars_path = Path('./tfvars')
    if tfvars_path.exists() and tfvars_path.is_dir():
        try:
            tfvars_path.rmdir()
        except OSError:
            shutil.rmtree(tfvars_path)
    tfvars_path.mkdir()

def builds_tfvars_for_sca(base_networking, project_type, waf_log_type, ip_block):
    path_to_download_in_repo = "https://raw.githubusercontent.com/7clouds-serverless-solutions/sca-tf-templates" \
                               "/master/tfvars_templates"

    path_to_download_in_repo += "/BaseNetworking" if base_networking else "/NoBaseNetworking"
    if type(base_networking) != bool:
        print("Error! Variable base_networking value must be bool. Stopping builder...")
        exit()
    if type(project_type) != int or (not (1 <= project_type <= 6)):
        print("Error! Variable project_type must be int between 1 and 6 (1, 2, 3, 4, 5 or 6). Stopping Builder...")
        exit()
    if type(waf_log_type) != int or (not (1 <= waf_log_type <= 6)):
        print("Error! Variable waf_log_type must be int between 1 and 6 (1, 2, 3, 4, 5 or 6). Stopping Builder...")
        exit()
    if type(ip_block) != bool:
        print("Error! Variable ip_block value must be bool. Stopping builder...")
        exit()

    if project_type == 1:
        path_to_download_in_repo = resolves_project_type_1(path_to_download_in_repo, waf_log_type, ip_block)

    if project_type == 2:
        path_to_download_in_repo += "/LambdaAPIGatewayCognito"
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

    if project_type == 3:
        path_to_download_in_repo += "/LambdaAPIGatewayCognitoMemCached"
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

    if project_type == 4:
        path_to_download_in_repo += "/LambdaAPIGatewayCognitoRedis"
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

    if project_type == 5:
        path_to_download_in_repo += "/LambdaAPIGatewayMemCached"
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

    if project_type == 6:
        path_to_download_in_repo += "/LambdaAPIGatewayRedis"
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

    path_to_download_in_repo += "/variables.tfvars"
    print(path_to_download_in_repo)
    response = requests.get(path_to_download_in_repo)
    open('./tfvars/variables.tfvars', 'wb').write(response.content)


