with open('server/scripts/modules/settings.mjs', 'r') as f:
    code = f.read()

import_str = "import { createAdvancedConfigUI } from './utils/advancedConfigUI.mjs';"
code = code.replace("import btnNavigateRefreshClick from '../index.mjs';", f"import btnNavigateRefreshClick from '../index.mjs';\n{import_str}")

code = code.replace("settingsSection.append(...settingHtml);", "settingsSection.append(...settingHtml);\n\n\tcreateAdvancedConfigUI();")

with open('server/scripts/modules/settings.mjs', 'w') as f:
    f.write(code)
