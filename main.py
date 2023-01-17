import requests
def builds_tfvars_for_SCA():
    url = "https://api.github.com/repos/7clouds-serverless-solutions/sca-tf-templates/contents/tfvars_templates"
    response = requests.get(url)

    if response.status_code == 200:
        contents = response.json()
        for item in contents:
            print(f"Download successful: \n {item['name']}")

    else:
        print(f"Error: {response.status_code}")

    base_networking = input("Do you want to build a project with Base Networking Resources? Type yes or no: ")
    if base_networking not in ["yes","no"]:
        print("Invalid input for base_networking, stopping builder...")
        return
    else:
        pass
    try:
        project_type = int(input("Which project type are we building? From 1 to 6: "))
        if project_type not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input for attribute project_type, stopping builder...")
            return
        else:
            pass
        waf_log_type = int(input("Which log type are we attaching to the project? \n0 for no logs \n1 for centralized logs \n2 for cloudwatch logs: "))
        if waf_log_type not in [0, 1, 2]:
            print("Invalid input for waf_log_type, stopping builder...")
            return
        else:
            pass
        ip_block = int(input("Which kind of WAF are we attaching to the project? \n1 Without IP Block \n2 With IP Block: "))
        if ip_block not in [1, 2]:
            print("Invalid input for ip_block, stopping builder...")
            return
        else:
            pass

    except ValueError:
        print("The fields project_type, waf_log_type and ip_block must be integers \n")
    return {"base_networking": base_networking, "project_type": project_type, "waf_log_type": waf_log_type, "ip_block": ip_block}

result = builds_tfvars_for_SCA()
if result:
    print(result["base_networking"])
    print(result["project_type"])
    print(result["waf_log_type"])
    print(result["ip_block"])
else:
    print("Function returned None")
