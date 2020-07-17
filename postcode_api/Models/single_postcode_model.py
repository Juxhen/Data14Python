class SinglePCModel:

    def __init__(self, single_pc_json):
        self.status = single_pc_json['status']
        self.result = single_pc_json['result']
        self.postcode = self.result['postcode']
        self.quality = self.result['quality']
        self.eastings = self.result['eastings']
        self.northings = self.result['northings']
        self.country = self.result['country']
        self.nhs_ha = self.result['nhs_ha']
        self.admin_county = self.result['admin_county']
        self.admin_ward = self.result['admin_ward']
        self.longitude = self.result['longitude']
        self.latitude = self.result['latitude']
        self.parliamentary_constituency = self.result['parliamentary_constituency']