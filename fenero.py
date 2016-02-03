import requests
import webbrowser


class APICall(object):
    def __init__(self):
        self.url = "https://manager.fenero.com/MobileApi/"

    # Returns a list of all campaigns and ACD queues.
    def get_campaigns_and_queues(self, user_id, app_token_id):
        req_type = "GetCampaignsAndQueues"
        payload = (('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Returns a list of all live chat queues.
    def get_live_chat_queues(self, user_id, app_token_id):
        req_type = "GetLiveChatQueues"
        payload = (('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Returns a list of all local and toll-free DIDs in the system.
    def get_dids(self, user_id, app_token_id):
        req_type = "GetDIDs"
        payload = (('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Returns a list of all dispositions in the system.
    def get_dispositions(self, user_id, app_token_id):
        req_type = "GetDispositions"
        payload = (('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Returns a list of all users in the system.
    def get_users(self, user_id, app_token_id):
        req_type = "GetUsers"
        payload = (('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Returns a combination of JSON arrays containing real-time call, agent, and time information.
    def get_realtime_stats(self, campaign_ids, group_ids, user_id, app_token_id):
        req_type = "GetRealtimeStats"
        campaign_ids = campaign_ids
        group_ids = group_ids
        payload = (('userId', user_id), ('campaignIds', campaign_ids), ('groupIds', group_ids),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Send a request to blind-monitor an agent's session. Values for the following parameters can be retrieved by
    # sending a call to GetRealtimeStats
    def monitor(self, session_id, server_ip, user_phone, agent_id, user_id, app_token_id):
        req_type = "Monitor"
        payload = (('userId', user_id), ('sessionId', session_id), ('serverIP', server_ip),
                   ('userPhone', user_phone), ('agentID', agent_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Similar to the Monitor command, except the callee on the receiving end of the userPhone will be able to actively
    # participate in the call and heard by both parties. Values for the following parameters can be retrieved by sending
    #  a call to GetRealtimeStats
    def barge(self, session_id, server_ip, user_phone, agent_id, user_id, app_token_id):
        req_type = "Barge"
        payload = (('userId', user_id), ('sessionId', session_id), ('serverIP', server_ip),
                   ('userPhone', user_phone), ('agentID', agent_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Returns a JSON formatted array of dialing lists currently in the system.
    def get_lists(self, campaign_ids, user_id, app_token_id):
        req_type = "GetLists"
        payload = (('userId', user_id), ('campaignIds', campaign_ids),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Create a new dialing list.
    def create_list(self, name, description, caller_id, campaign_id, reset_times, active, user_id, app_token_id):
        req_type = "CreateList"
        payload = (('name', name), ('description', description), ('callerId', caller_id),
                   ('campaignId', campaign_id), ('resetTimes', reset_times), ('active', active),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Copies the custom field definitions from an existing list to the destination list specified.
    def copy_custom_fields(self, source_list_id, destination_list_id, user_id, app_token_id):
        req_type = "CopyCustomFields"
        payload = (('sourceListId', source_list_id), ('destinationListId', destination_list_id),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Sets an inactive list in an active state. If there are any dialable leads in the system and other rules are met
    # (e.g. recycling rules, campaign hours of operations, available agents, etc), this will begin dialing the records
    # in the list.
    def start_list(self, list_id, user_id, app_token_id):
        req_type = "StartList"
        payload = (('userId', user_id), ('listId', list_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Sets an active list to an inactive state. Dialing operations (if any) will be stopped immediately (any currently
    # active calls will continue to be processed).
    def stop_list(self, list_id, user_id, app_token_id):
        req_type = "StopList"
        payload = (('userId', user_id), ('listId', list_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Searches the quality assurance system for all call recordings within the specified date range, for the given
    # campaign/ACD queue.
    def get_recordings(self, start_date, end_date, campaign_ids, user_id, app_token_id):
        req_type = "GetRecordings"
        payload = (('userId', user_id), ('startDate', start_date), ('endDate', end_date),
                   ('campaignIds', campaign_ids), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        print(r.url)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.json()

    # Given a recording Id, streams or immediately downloads the recording's audio file.
    def stream_recording(self, recording_id, user_id, app_token_id):
        req_type = "StreamRecording"
        payload = (('userId', user_id), ('recordingId', recording_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload, stream=True)
        with open(recording_id, 'wb') as f:  # Save .wav stream to disk
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
            webbrowser.open(recording_id)  # Open file in default browser

    # Executes the Agent Activity Summary report using the filters specified as parameters and returns raw output as
    # comma-separated values
    def report_agent_activity_summary(self, start_date, end_date, users, campaign_ids, tz_offset, user_id,
                                      app_token_id):
        req_type = "ReportAgentActivitySummary"
        payload = (('startDate', start_date), ('endDate', end_date), ('users', users),
                   ('campaignIds', campaign_ids), ('tzOffset', tz_offset), ('userId', user_id),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        print(r.url)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Agent Aux Detail report using the filters specified as parameters and returns raw output as
    # comma-separated values
    def report_agent_aux_detail(self, start_date, end_date, report_type, users, campaign_ids, tz_offset, user_id,
                                app_token_id):
        req_type = "ReportAgentAuxDetail"
        payload = (('startDate', start_date), ('endDate', end_date), ('reportType', report_type),
                   ('users', users), ('campaignIds', campaign_ids), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        print(r.url)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Agent Performance Detail report using the filters specified as parameters and returns raw output as
    # comma-separated values
    def report_agent_performance_detail(self, start_date, end_date, report_type, users, campaign_ids, queue_ids,
                                        tz_offset, user_id, app_token_id):
        req_type = "ReportAgentPerformanceDetail"
        payload = (('startDate', start_date), ('endDate', end_date), ('reportType', report_type),
                   ('users', users), ('campaignIds', campaign_ids), ('queueIds', queue_ids),
                   ('tzOffset', tz_offset), ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Agent Log report using the filters specified as parameters and returns raw output as comma-separated
    # values
    def report_agent_log(self, start_date, end_date, users, campaign_ids, tz_offset, user_id, app_token_id):
        req_type = "ReportAgentLog"
        payload = (('startDate', start_date), ('endDate', end_date), ('users', users),
                   ('campaignIds', campaign_ids), ('tzOffset', tz_offset), ('userId', user_id),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        print(r.url)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Agent Staff Time report using the filters specified as parameters and returns raw output as
    # comma-separated values
    def report_agent_staff_time(self, start_date, end_date, users, tz_offset, user_id, app_token_id):
        req_type = "ReportAgentStaffTime"
        payload = (('startDate', start_date), ('endDate', end_date), ('users', users), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Agent Disposition report using the filters specified as parameters and returns raw output as
    # comma-separated values
    def report_agent_disposition(self, start_date, end_date, users, tz_offset, user_id, app_token_id):
        req_type = "ReportAgentDisposition"
        payload = (('startDate', start_date), ('endDate', end_date), ('users', users), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Campaign DNC report using the filters specified as parameters and returns raw output as
    # comma-separated values
    def report_campaign_dnc(self, campaign_ids, user_id, app_token_id):
        req_type = "ReportCampaignDNC"
        payload = (('campaignIds', campaign_ids), ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Call Detail Records (Inbound) report using the filters specified as parameters and returns raw output
    # as comma-separated values. This report is the source of all inbound call-related billing activity.
    def report_call_detail_records_inbound(self, start_date, end_date, tz_offset, user_id, app_token_id):
        req_type = "ReportCallDetailRecordsInbound"
        payload = (('startDate', start_date), ('endDate', end_date), ('tzOffset', tz_offset), ('userId', user_id),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Call Detail Records (Outbound) report using the filters specified as parameters and returns raw
    # output as comma-separated values. This report is the source of all outbound call-related billing activity.
    def report_call_detail_records_outbound(self, start_date, end_date, tz_offset, user_id, app_token_id):
        req_type = "ReportCallDetailRecordsInbound"
        payload = (('startDate', start_date), ('endDate', end_date), ('tzOffset', tz_offset), ('userId', user_id),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Call Detail Records (Inbound&Outbound) report using the filters specified as parameters and returns
    # raw output as comma-separated values. This report is the source of all call-related billing activity.
    def report_call_detail_records_combined(self, start_date, end_date, tz_offset, user_id, app_token_id):
        req_type = "ReportCallDetailRecordsCombined"
        payload = (('startDate', start_date), ('endDate', end_date), ('tzOffset', tz_offset), ('userId', user_id),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Call Detail Usage report using the filters specified as parameters and returns raw output as
    # comma-separated values. This report is a summarized view of the Call Detail Records (Inbound&Outbound) reports.
    def report_call_detail_usage(self, start_date, end_date, report_type, users, campaign_ids, queue_ids, tz_offset,
                                 user_id, app_token_id):
        req_type = "ReportCallDetailUsage"
        payload = (('startDate', start_date), ('endDate', end_date), ('reportType', report_type), ('users', users),
                   ('campaignIds', campaign_ids), ('queue_ids', queue_ids), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Live Chat Log report using the filters specified as parameters and returns raw output as
    # comma-separated values.
    def report_live_chat_log(self, start_date, end_date, chat_queue_ids, tz_offset, user_id, app_token_id):
        req_type = "ReportLiveChatLog"
        payload = (('startDate', start_date), ('endDate', end_date), ('chatQueueIds', chat_queue_ids),
                   ('tzOffset', tz_offset), ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Interaction Detail report using the filters specified as parameters and returns raw output as
    # comma-separated values.
    def report_interaction_detail(self, start_date, end_date, list_ids, disposition_ids, campaign_ids, tz_offset,
                                  user_id, app_token_id):
        req_type = "ReportInteractionDetail"
        payload = (('startDate', start_date), ('endDate', end_date), ('listIds', list_ids),
                   ('dispositionIds', disposition_ids), ('campaignIds', campaign_ids), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Interaction Detail Log report using the filters specified as parameters and returns raw output as
    # comma-separated values.
    def report_interaction_detail_log(self, start_date, end_date, list_ids, disposition_ids, campaign_ids, tz_offset,
                                      user_id, app_token_id):
        req_type = "ReportInteractionDetailLog"
        payload = (('startDate', start_date), ('endDate', end_date), ('listIds', list_ids),
                   ('dispositionIds', disposition_ids), ('campaignIds', campaign_ids), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the System Call Log report using the filters specified as parameters and returns raw output as
    # comma-separated values
    def report_system_call_log(self, start_date, end_date, queue_ids, campaign_ids, tz_offset, user_id, app_token_id):
        req_type = "ReportSystemCallLog"
        payload = (('startDate', start_date), ('endDate', end_date), ('queueIds', queue_ids),
                   ('campaignIds', campaign_ids), ('tzOffset', tz_offset), ('userId', user_id),
                   ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Lead Detail report using the filters specified as parameters and returns raw output as
    # comma-separated values.
    def report_lead_detail(self, start_date, end_date, list_ids, queue_ids, campaign_ids, tz_offset, user_id,
                           app_token_id):
        req_type = "ReportLeadDetail"
        payload = (('startDate', start_date), ('endDate', end_date), ('listIds', list_ids),
                   ('queueIds', queue_ids), ('campaignIds', campaign_ids), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the Disposition Summary report using the filters specified as parameters and returns raw output as
    # comma-separated values.
    def report_dispositions_summary(self, start_date, end_date, list_ids, queue_ids, campaign_ids, tz_offset, user_id,
                                    app_token_id):
        req_type = "ReportDispositionSummary"
        payload = (('startDate', start_date), ('endDate', end_date), ('listIds', list_ids),
                   ('queueIds', queue_ids), ('campaignIds', campaign_ids), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text

    # Executes the outbound-specific Flash Summary report using the filters specified as parameters and returns raw
    # output as comma-separated values.
    def report_flash_summary(self, start_date, end_date, list_ids, tz_offset, user_id, app_token_id):
        req_type = "ReportFlashSummary"
        payload = (('startDate', start_date), ('endDate', end_date), ('listIds', list_ids), ('tzOffset', tz_offset),
                   ('userId', user_id), ('appTokenId', app_token_id))
        r = requests.get(self.url + req_type, params=payload)
        if r.status_code != 200:
            print("Error: " + str(r.status_code))
        else:
            return r.text
