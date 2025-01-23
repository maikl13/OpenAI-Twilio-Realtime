import json

function_mapping = {}  # {"function_name": function_to_call}


async def execute_tool(json_data):
    function_name = json_data.get("name")
    arguments = json.loads(json_data.get("arguments"))

    if function_name in function_mapping:
        function_to_call = function_mapping[function_name]
        result = await function_to_call(arguments)
        return result
    else:
        return {"error": f"Function {function_name} not found."}
