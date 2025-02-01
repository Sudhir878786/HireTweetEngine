class BaseScraper:
    def fetch_jobs(self):
        raise NotImplementedError("This method should be overridden by the subclass.")
    
    def fetch_job_details(self, job_url):
        raise NotImplementedError("This method should be overridden by the subclass.")
