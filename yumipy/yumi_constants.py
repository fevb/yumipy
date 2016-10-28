'''
Constants for YuMi interface and control
Author: Jacky Liang
'''
import logging
from yumi_state import YuMiState
from alan.core import RigidTransform

class YuMiConstants:

    IP = '192.168.125.1'
    PORT_L = 5000
    PORT_L_SUB = 5010
    PORT_R = 5001
    PORT_R_SUB = 5011
    
    BUFSIZE = 4096
    MOTION_TIMEOUT = 8
    COMM_TIMEOUT = 5
    PROCESS_TIMEOUT = 10

    GRASP_COUNTER_PATH = '/home/autolab/Public/alan/grasp_counts'

    # used to rate limit real-time YuMi controls (in seconds)
    COMM_PERIOD = 0.04 
    
    DEBUG = False
    LOGGING_LEVEL = logging.DEBUG
    
    # reset mechanism
    RESET_RIGHT_COMM = '/dev/ttyACM0'
    RESET_BAUDRATE = 115200
    
    CMD_CODES = {
        'ping': 0,
        'goto_pose_linear':1,
        'goto_joints': 2,
        'get_pose': 3,
        'get_joints':4,
        'goto_pose':5,
        'set_tool':6,
        'set_speed':8,
        'set_zone':9,
        
        'goto_pose_sync':11,
        'goto_joints_sync':12,
        'goto_pose_delta':13,
        
        'close_gripper': 20,
        'open_gripper': 21,
        'calibrate_gripper': 22,
        'set_gripper_max_speed': 23,
        'set_gripper_force': 24,
        'move_gripper': 25,
        'get_gripper_width': 26,
        
        'set_circ_point':35,
        'move_by_circ_point':36,
        'buffer_add': 30,
        'buffer_clear': 31,
        'buffer_size': 32,
        'buffer_move': 33,
        
        'is_pose_reachable': 40,
        'is_joints_reachable': 41,

        'close_connection': 99,
        
        'reset_home': 100,
    }
    
    RES_CODES = {
        'failure': 0,
        'success': 1
    }

    SUB_CODES = {
        'pose': 0,
        'state': 1
    }
    MOVEIT_PLANNER_IDS = { 
        'SBL': 'SBLkConfigDefault',
        'EST': 'ESTkConfigDefault',
        'LBKPIECE': 'LBKPIECEkConfigDefault',
        'BKPIECE': 'BKPIECEkConfigDefault',
        'KPIECE': 'KPIECEkConfigDefault',    
        'RRT': 'RRTkConfigDefault',    
        'RRTConnect': 'RRTConnectkConfigDefault',
        'RRTstar': 'RRTstarkConfigDefault',
        'TRRT': 'TRRTkConfigDefault',
        'PRM': 'PRMkConfigDefault',
        'PRMstar': 'PRMstarkConfigDefault'
    }
    MOVEIT_PLANNING_REFERENCE_FRAME = 'yumi_body'
    T_GRIPPER_HAND = RigidTransform(translation=[0,0,-0.157], from_frame='gripper', to_frame='gripper')
    
    TCP_ABB_GRIPPER = RigidTransform(translation=[0,0,0.136])
    TCP_ABB_GRASP_GRIPPER = RigidTransform(translation=[0,0,0.136-0.0065])
    TCP_LONG_GRIPPER = RigidTransform(translation=[0,0,(136-56+88-12)/1000.])
    TCP_DEFAULT_GRIPPER = RigidTransform(translation=[0,0,(136-56+88-12)/1000.])
    
    L_HOME_STATE = YuMiState([0, -130, 30, 0, 40, 0, 135])
    L_HOME_POSE = RigidTransform(translation=[0.123, 0.147, 0.124], rotation=[0.06551, 0.84892, -0.11147, 0.51246])
    
    R_HOME_STATE = YuMiState([0, -130, 30, 0, 40, 0, -135])
    R_HOME_POSE = RigidTransform(translation=[-0.0101, -0.1816, 0.19775], rotation=[-0.52426, 0.06481, -0.84133, -0.11456])
    
    R_FORWARD_STATE = YuMiState([9.66, -133.36, 34.69, -13.19, 28.85, 28.81, -110.18])
    R_FORWARD_POSE = RigidTransform(translation=[0.07058, -0.26519, 0.19775], rotation=[-0.52425, 0.0648, -0.84133, -0.11454])

    R_AWAY_POSE = RigidTransform(translation=[0.15, -0.4, 0.22], rotation=[0.38572, 0.39318, 0.60945, 0.57027])
    L_AWAY_POSE = RigidTransform(translation=[0.30, 0.12, 0.16], rotation=[0.21353, -0.37697, 0.78321, -0.44596])
    
    L_RAISED_STATE = YuMiState([5.5, -99.46, 20.52, -21.03, 67, -22.31, 110.11])
    L_RAISED_POSE = RigidTransform(translation=[-0.0073, 0.39902, 0.31828], rotation=[0.54882, 0.07398, 0.82585, -0.10630])
    
    L_FORWARD_STATE = YuMiState([-21.71, -142.45, 43.82, 31.14, 10.43, -40.67, 106.63])
    L_FORWARD_POSE = RigidTransform(translation=[0.13885, 0.21543, 0.19774], rotation=[0.55491, 0.07064, 0.82274, -0.1009])

    L_PREDROP_POSE = RigidTransform(translation=[0.596, 0.185, 0.259],
                                    rotation=[0.09815, -0.20528, 0.97156, -0.06565])
    L_DROP_POSES = [
        RigidTransform(translation=[0.44, 0.455, 0.26], rotation=[0.09078, -0.31101, 0.91820, -0.22790]),
        RigidTransform(translation=[0.44, 0.385, 0.26], rotation=[0.09078, -0.31101, 0.91820, -0.22790]),
        RigidTransform(translation=[0.31, 0.385, 0.26], rotation=[0.09078, -0.31101, 0.91820, -0.22790]),
        RigidTransform(translation=[0.31, 0.455, 0.26], rotation=[0.09078, -0.31101, 0.91820, -0.22790])
    ]

    BOX_CLOSE_SEQUENCE = [
        #('L', RigidTransform(translation=[0.071, 0.385, 0.118], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        #('L', RigidTransform(translation=[0.213, 0.385, 0.118], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        #('L', RigidTransform(translation=[0.213, 0.385, 0.156], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        #('L', RigidTransform(translation=[0.323, 0.385, 0.156], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        #('L', RigidTransform(translation=[0.323, 0.385, 0.144], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('R', [0, 0.300, 0]),
        ('R', [0.100, 0, 0]),
        ('R', YuMiState([111.30, -65.37, -29.93, -50.53, 65.41, -94.59, -68.84])),
        ('R', YuMiState([147.13, -76.28, -58.98, -13.85, 54.95, 54.95, -96.95])),
        ('R', [0, 0, 0.070]),
        ('R', [-0.074, 0, 0]),
        ('R', [0, -0.012, 0]),
        ('R', [0, 0, -0.040]),
        ('R', YuMiState([132.32, -56.98, -8.13, -72.42, 36.44, 135.16, -99.36])),
        ('R', YuMiState([146.72, -57.09, -9.44, -101.74, 69.26, 155.98, -98.41])),
        ('R', YuMiState([168.36, -64.12, -23.60, -118.0, 97.50, 163.97, -102.95])),
        ('R', YuMiState([168.37, -59.60, 2.63, -146.15, 95.29, 199.63, -129.70])),
        ('R', YuMiState([168.37, -82.24, -10.81, -196.49, 115.92, 199.63, -148.06])),
        ('L', RigidTransform(translation=[0.323, 0.385, 0.203], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.203, 0.478, 0.203], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.203, 0.478, 0.092], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.305, 0.478, 0.092], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.305, 0.478, 0.183], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.305, 0.359, 0.183], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.305, 0.359, 0.149], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.425, 0.359, 0.149], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.425, 0.359, 0.245], rotation=[0.06744, 0.84050, -0.11086, 0.52604])),
        ('L', RigidTransform(translation=[0.265, 0.445, 0.245], rotation=[0.06744, 0.84050, -0.11086, 0.52604]))]
    """
        ('R', RigidTransform(translation=[0.490, 0.277, 0.264], rotation=[0.44160, 0.57131, 0.53374, 0.44013])),
        ('R', RigidTransform(translation=[0.490, -0.20, 0.264], rotation=[0.09799, -0.67708, -0.72314, -0.09502])),
        ('R', RigidTransform(translation=[0.428, 0.128, 0.147], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.428, 0.164, 0.147], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.428, 0.164, 0.196], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.428, 0.277, 0.196], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.428, 0.277, 0.153], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.428, 0.277, 0.158], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.499, 0.277, 0.158], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.337, 0.277, 0.158], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.337, 0.277, 0.226], rotation=[0.30215, -0.62096, -0.66425, -0.28615])),
        ('R', RigidTransform(translation=[0.493, 0.146, 0.226], rotation=[0.30215, -0.62096, -0.66425, -0.28615]))
    ]
"""