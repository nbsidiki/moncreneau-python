from typing import List, Optional, Dict, Any


class Appointments:
    """Resource for managing appointments"""
    
    def __init__(self, http_client):
        self.http = http_client
    
    def create(
        self,
        department_id: str,
        date_time: str,
        user_name: str,
        user_phone: str,
        user_email: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new appointment
        
        Args:
            department_id: ID of the department
            date_time: Appointment date and time (ISO 8601 format)
            user_name: Full name of the patient
            user_phone: Phone number (international format, e.g. +224621234567)
            user_email: Email address (optional)
            notes: Additional notes (optional)
        
        Returns:
            Created appointment data
        """
        data = {
            'departmentId': department_id,
            'dateTime': date_time,
            'userName': user_name,
            'userPhone': user_phone
        }
        
        if user_email:
            data['userEmail'] = user_email
        if notes:
            data['notes'] = notes
        
        return self.http.post('/appointments', data)
    
    def retrieve(self, id: str) -> Dict[str, Any]:
        """
        Retrieve an appointment by ID
        
        Args:
            id: Appointment ID
        
        Returns:
            Appointment data
        """
        return self.http.get(f'/appointments/{id}')
    
    def list(
        self,
        page: int = 0,
        size: int = 50,
        status: Optional[str] = None,
        department_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        List appointments with pagination and filters
        
        Args:
            page: Page number (0-indexed)
            size: Number of items per page (max 100)
            status: Filter by status (SCHEDULED, COMPLETED, CANCELLED, etc.)
            department_id: Filter by department ID
            start_date: Filter appointments after this date
            end_date: Filter appointments before this date
        
        Returns:
            Paginated list of appointments
        """
        params = {'page': page, 'size': size}
        
        if status:
            params['status'] = status
        if department_id:
            params['departmentId'] = department_id
        if start_date:
            params['startDate'] = start_date
        if end_date:
            params['endDate'] = end_date
        
        return self.http.get('/appointments', params)
    
    def cancel(self, id: str) -> None:
        """
        Cancel an appointment
        
        Args:
            id: Appointment ID
        """
        self.http.delete(f'/appointments/{id}')
