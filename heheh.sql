CREATE OR REPLACE PACKAGE BODY JOB_PKG AS 
PROCEDURE validate_salary ( --private procedure for salary validation     
	v_min_salary IN jobs.min_salary%TYPE, 
   	v_max_salary IN jobs.max_salary%TYPE 
) 
 
IS BEGIN --this procedure is raised when the rule is violated 
    IF v_max_salary <= v_min_salary THEN 
        RAISE_APPLICATION_ERROR(-20001, 'Your max salary must be greater than min salary.'); 
    END IF; 
END validate_salary; 
 
PROCEDURE ADD_JOB ( --public procedure to add a new job
    h_job_id      IN jobs.job_id%TYPE, 
    h_job_title   IN jobs.job_title%TYPE, 
    h_min_salary  IN jobs.min_salary%TYPE, 
    h_max_salary  IN jobs.max_salary%TYPE 
) 
 
IS BEGIN 
    validate_salary(h_min_salary, h_max_salary); --validate first the salary before inserting a new record 
 
    INSERT INTO jobs (job_id, job_title, min_salary, max_salary) 
    VALUES (h_job_id, h_job_title, h_min_salary, h_max_salary); 
 
    COMMIT; 
END ADD_JOB; 

PROCEDURE UPD_JOB ( --public procedure to update the job title
    h_job_id        IN jobs.job_id%TYPE,
    h_new_title        IN jobs.job_title%TYPE
)
IS 
    v_rows_updated NUMBER;  --store affected rows
BEGIN
    UPDATE jobs
    SET job_title = h_new_title
    WHERE job_id = h_job_id;

    v_rows_updated := SQL%ROWCOUNT; --get the numbers of updated rows

    IF v_rows_updated = 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'No job found with the given job ID.');
    END IF;

    COMMIT;
END UPD_JOB;
END JOB_PKG;