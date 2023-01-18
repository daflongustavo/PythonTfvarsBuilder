import requests
from pathlib import Path
import shutil
def creates_new_directory_tfvars():
    tfvars_path = Path('./tfvars')
    if tfvars_path.exists() and tfvars_path.is_dir():
        try:
            tfvars_path.rmdir()
        except OSError:
            shutil.rmtree(tfvars_path)
    tfvars_path.mkdir()

def builds_tfvars_for_SCA (base_networking, project_type, waf_log_type, ip_block):
    path_to_download_in_repo = "https://raw.githubusercontent.com/7clouds-serverless-solutions/sca-tf-templates/master/tfvars_templates"

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

    path_to_download_in_repo += "/variables.tfvars"
    response = requests.get(path_to_download_in_repo)
    open('./tfvars/variables.tfvars', 'wb').write(response.content)


creates_new_directory_tfvars()

print("aaaaaa")
builds_tfvars_for_SCA(base_networking=True, project_type=1, waf_log_type=1, ip_block=True)

