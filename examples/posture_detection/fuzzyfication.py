def _convertion_vFuzzy_to_vInterval_start(x):
    return x*(1.0 - 0.25 * 2 * min(x, 1-x))


def _convertion_vFuzzy_to_vInterval_end(x):
    return (x*(1.0 - 0.25 * 2 * min(x, 1-x))) + (0.25 * 2 * min(x, 1-x))


def _fun_HW_low(x):
    if x <= 0.5:
        x = 1
    elif 0.5 < x <= 2:
        x = (2 - x) / 1.5
    elif x > 2:
        x = 0
    return x


def fun_HW_low(x):
    if type(x) is tuple:
        return _fun_HW_low(x[0]), _fun_HW_low(x[1])
    else:
        return _fun_HW_low(x)


def fun_HW_low_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_HW_low(x))


def fun_HW_low_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_HW_low(x))


def _fun_HW_med(x):
    if x <= 0.5 or x > 3.2:
        x = 0
    elif 0.5 < x <= 2:
        x = (x - 0.5) / 1.5
    elif 2 < x <= 3.2:
        x = (3.2 - x) / 1.2
    return x


def fun_HW_med(x):
    if type(x) is tuple:
        return _fun_HW_med(x[0]), _fun_HW_med(x[1])
    else:
        return _fun_HW_med(x)


def fun_HW_med_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_HW_med(x))


def fun_HW_med_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_HW_med(x))


def _fun_HW_high(x):
    if x <= 2:
        x = 0
    elif 2 < x <= 3.2:
        x = (x - 2) / 1.2
    elif x > 3.2:
        x = 1
    return x


def fun_HW_high(x):
    if type(x) is tuple:
        return _fun_HW_high(x[0]), _fun_HW_high(x[1])
    else:
        return _fun_HW_high(x)


def fun_HW_high_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_HW_high(x))


def fun_HW_high_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_HW_high(x))


def _fun_HHmax_low(x):
    if x <= 0.25:
        x = 1
    elif 0.25 < x <= 0.6:
        x = (0.6 - x) / 0.35
    elif x > 0.6:
        x = 0
    return x


def fun_HHmax_low(x):
    if type(x) is tuple:
        return _fun_HHmax_low(x[0]), _fun_HHmax_low(x[1])
    else:
        return _fun_HHmax_low(x)

def fun_HHmax_low_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_HHmax_low(x))


def fun_HHmax_low_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_HHmax_low(x))


def _fun_HHmax_med(x):
    if x <= 0.25 or x > 1:
        x = 0
    elif 0.25 < x <= 0.6:
        x = (x - 0.25) / 0.35
    elif 0.6 < x <= 1:
        x = (1 - x) / 0.35
        if x > 1:
            x = 1
    return x


def fun_HHmax_med(x):
    if type(x) is tuple:
        return _fun_HHmax_med(x[0]), _fun_HHmax_med(x[1])
    else:
        return _fun_HHmax_med(x)


def fun_HHmax_med_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_HHmax_med(x))


def fun_HHmax_med_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_HHmax_med(x))


def _fun_HHmax_high(x):
    if x <= 0.6:
        x = 0
    elif 0.6 < x <= 1:
        x = (x - 0.6) / 0.4
    elif x > 1:
        x = 1
    return x


def fun_HHmax_high(x):
    if type(x) is tuple:
        return _fun_HHmax_high(x[0]), _fun_HHmax_high(x[1])
    else:
        return _fun_HHmax_high(x)


def fun_HHmax_high_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_HHmax_high(x))


def fun_HHmax_high_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_HHmax_high(x))


def _fun_sigma_low(x):
    if x <= 260:
        x = 1
    elif 260 < x <= 310:
        x = (310 - x) / (310 - 260)
    elif x > 310:
        x = 0
    return x


def fun_sigma_low(x):
    if type(x) is tuple:
        return _fun_sigma_low(x[0]), _fun_sigma_low(x[1])
    else:
        return _fun_sigma_low(x)


def fun_sigma_low_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_sigma_low(x))


def fun_sigma_low_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_sigma_low(x))


def _fun_sigma_med(x):
    if x <= 260 or x > 410:
        x = 0
    elif 260 < x <= 310:
        x = (x - 260) / (310 - 260)
    elif 310 < x <= 410:
        x = (410 - x) / (410 - 310)
    return x


def fun_sigma_med(x):
    if type(x) is tuple:
        return _fun_sigma_med(x[0]), _fun_sigma_med(x[1])
    else:
        return _fun_sigma_med(x)


def fun_sigma_med_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_sigma_med(x))


def fun_sigma_med_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_sigma_med(x))


def _fun_sigma_high(x):
    if x <= 310:
        x = 0
    elif 310 < x <= 410:
        x = (x - 310) / (410 - 310)
    elif x > 410:
        x = 1
    return x


def fun_sigma_high(x):
    if type(x) is tuple:
        return _fun_sigma_high(x[0]), _fun_HHmax_high(x[1])
    else:
        return _fun_sigma_high(x)


def fun_sigma_high_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_sigma_high(x))


def fun_sigma_high_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_sigma_high(x))


def _fun_P40_low(x):
    if x <= 0.18:
        x = 1
    elif 0.18 < x <= 0.42:
        x = (0.42 - x) / (0.42 - 0.18)
    elif x > 0.42:
        x = 0
    return x


def fun_P40_low(x):
    if type(x) is tuple:
        return _fun_P40_low(x[0]), _fun_P40_low(x[1])
    else:
        return _fun_P40_low(x)


def fun_P40_low_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_P40_low(x))


def fun_P40_low_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_P40_low(x))


def _fun_P40_med(x):
    if x <= 0.18 or x > 0.68:
        x = 0
    elif 0.18 < x <= 0.42:
        x = (x - 0.18) / (0.42 - 0.18)
    elif 0.42 < x <= 0.68:
        x = (0.68 - x) / (0.68 - 0.42)
    return x


def fun_P40_med(x):
    if type(x) is tuple:
        return _fun_P40_med(x[0]), _fun_P40_med(x[1])
    else:
        return _fun_P40_med(x)


def fun_P40_med_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_P40_med(x))


def fun_P40_med_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_P40_med(x))


def _fun_P40_high(x):
    if x <= 0.42:
        x = 0
    elif 0.42 < x <= 0.68:
        x = (x - 0.42) / (0.68 - 0.42)
    elif x > 0.68:
        x = 1
    return x


def fun_P40_high(x):
    if type(x) is tuple:
        return _fun_P40_high(x[0]), _fun_P40_high(x[1])
    else:
        return _fun_P40_high(x)


def fun_P40_high_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_P40_high(x))


def fun_P40_high_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_P40_high(x))


def _fun_Pose_isLy(x):
    if x <= 0.22:
        return 1
    elif 0.22 < x <= 0.5:
        return (0.5 - x) / (0.5 - 0.22)
    elif x > 0.5:
        return 0


def fun_Pose_isLy(x):
    if type(x) is tuple:
        return _fun_Pose_isLy(x[0]), _fun_Pose_isLy(x[1])
    else:
        return _fun_Pose_isLy(x)


def fun_Pose_isLy_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_Pose_isLy(x))


def fun_Pose_isLy_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_Pose_isLy(x))


def _fun_Pose_mayLy(x):
    if x <= 0.22 or x > 0.77:
        return 0
    elif 0.22 < x <= 0.5:
        return (x - 0.22) / (0.5 - 0.22)
    elif 0.5 < x <= 0.77:
        return (0.77 - x) / (0.77 - 0.5)


def fun_Pose_mayLy(x):
    if type(x) is tuple:
        return _fun_Pose_mayLy(x[0]), _fun_Pose_mayLy(x[1])
    else:
        return _fun_Pose_mayLy(x)


def fun_Pose_mayLy_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_Pose_mayLy(x))


def fun_Pose_mayLy_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_Pose_mayLy(x))


def _fun_Pose_notLy(x):
    if x > 0.77:
        return 1
    elif 0.5 < x <= 0.77:
        return (x - 0.5) / (0.77 - 0.5)
    elif x <= 0.5:
        return 0


def fun_Pose_notLy(x):
    if type(x) is tuple:
        return _fun_Pose_notLy(x[0]), _fun_Pose_notLy(x[1])
    else:
        return _fun_Pose_notLy(x)


def fun_Pose_notLy_start(x):
    return _convertion_vFuzzy_to_vInterval_start(_fun_Pose_notLy(x))


def fun_Pose_notLy_end(x):
    return _convertion_vFuzzy_to_vInterval_end(_fun_Pose_notLy(x))