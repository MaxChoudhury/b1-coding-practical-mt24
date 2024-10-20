# control.py

class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0.0  # To store the previous error

    def control_action(self, reference: float, current_depth: float) -> float:
        # Calculate the current error
        current_error = reference - current_depth

        # Calculate the control action
        u = self.kp * current_error + self.kd * (current_error - self.previous_error)

        # Print for debugging purposes
        print(f"Reference: {reference}, Current Depth: {current_depth}, Control Action: {u}")

        # Update previous error for next iteration
        self.previous_error = current_error

        return u
